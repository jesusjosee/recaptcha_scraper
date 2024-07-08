# app/services/scraper_service.py

from playwright.sync_api import Playwright
from app.services.captcha_solver import CaptchaSolver
import os

class ScraperService:
    def __init__(self, captcha_solver: CaptchaSolver):
        self.captcha_solver = captcha_solver

    def scrape(self, playwright: Playwright, url: str) -> str:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(locale="es-ES")
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")

        try:
            recaptcha_iframe = page.frame_locator('iframe[title="reCAPTCHA"]')
            recaptcha_iframe.locator(".recaptcha-checkbox-border").click()

            page.wait_for_selector('iframe[title="El reCAPTCHA caduca dentro de dos minutos"]')
            challenge_iframe = page.frame_locator('iframe[title="El reCAPTCHA caduca dentro de dos minutos"]')

            if challenge_iframe.locator('.rc-doscaptcha-header').is_visible():
                return "No se puede resolver el reCAPTCHA por audio. Inténtelo más tarde."

            challenge_iframe.locator("#recaptcha-audio-button").click()

            with page.expect_popup() as page1_info:
                challenge_iframe.locator('.rc-audiochallenge-tdownload-link').click()
            page1 = page1_info.value
            audio_url = page1.url
            page1.close()

            audio_text = self.captcha_solver.solve_audio_challenge(audio_url)

            if audio_text:
                challenge_iframe.locator("#audio-response").fill(audio_text)
                challenge_iframe.locator("#recaptcha-verify-button").click()

                page.locator("#recaptcha-demo-submit").click()

                return page.text_content(".recaptcha-success")

            return "No se puede procesar el captcha"
        except Exception as e:
            # Create output directory if it doesn't exist
            output_dir = "output_captcha"
            os.makedirs(output_dir, exist_ok=True)

            # Save screenshot and HTML
            page.screenshot(path=os.path.join(output_dir, "error_screenshot.png"))
            with open(os.path.join(output_dir, "error_page.html"), "w", encoding="utf-8") as f:
                f.write(page.content())

            # Log the error
            print(f"Error: {e}")
            raise

        finally:
            browser.close()
