import pytest
from unittest.mock import MagicMock
from playwright.sync_api import sync_playwright
from app.services.scraper_service import ScraperService
from app.services.captcha_solver import CaptchaSolver

class MockCaptchaSolver:
    def solve_audio_challenge(self, url):
        return "mock audio text"

@pytest.fixture
def scraper_service():
    captcha_solver = MockCaptchaSolver()
    return ScraperService(captcha_solver)

def test_scrape_success(scraper_service):
    with sync_playwright() as p:
        result = scraper_service.scrape(p, "https://www.google.com/recaptcha/api2/demo")
        assert "Success" in result

def test_scrape_failure(scraper_service):
    scraper_service.captcha_solver.solve_audio_challenge = MagicMock(return_value=None)
    with pytest.raises(Exception):
        with sync_playwright() as p:
            scraper_service.scrape(p, "https://www.google.com/recaptcha/api2/demo")
