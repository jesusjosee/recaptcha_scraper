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

