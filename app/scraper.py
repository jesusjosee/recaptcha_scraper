# app/scraper.py

import time
from playwright.sync_api import sync_playwright

class Scraper:
    def __init__(self, resolver):
        self.resolver = resolver

    def scrape(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            # Navigate to page with reCAPTCHA
            page.goto("https://www.google.com/recaptcha/api2/demo")
            
            # Wait for the page and resources to load completely
            page.wait_for_load_state("networkidle")
            
            # Wait for the reCAPTCHA iframe to be visible
            recaptcha_iframe = page.frame_locator('iframe[title="reCAPTCHA"]')
            
            # Wait for the checkbox inside the iframe to be visible and click on it
            checkbox = recaptcha_iframe.locator(".recaptcha-checkbox-border")
            checkbox.click()
            print("Se hizo clic en el checkbox del reCAPTCHA.")
            
            # Wait for the reCAPTCHA to be completed manually
            time.sleep(2)
            
            # Simulate form submission
            submit_button = page.locator("#recaptcha-demo-submit")
            submit_button.click()
            
            # Wait for the form to submit and get the response
            page.wait_for_load_state("networkidle")
            response = page.text_content(".recaptcha-success")
            print(f"Respuesta del formulario: {response}")
            
            browser.close()

            return response
