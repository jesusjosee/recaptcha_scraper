from .base_resolver import BaseResolver
from playwright.sync_api import Page

class RecaptchaV2CheckboxResolver(BaseResolver):
    def resolve(self, page: Page) -> bool:
        try:
            iframe = page.frame_locator('iframe[title="reCAPTCHA"]')
            checkbox = iframe.locator(".recaptcha-checkbox-border")
            checkbox.click()
            print("click en checkbox")
            # Wait for reCAPTCHA to be solved manually
            page.wait_for_timeout(5000)
            return True
        except Exception as e:
            print(f"Error solving reCAPTCHA: {e}")
            return False
