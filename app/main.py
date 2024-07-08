from fastapi import FastAPI, HTTPException
from app.schemas.scrape_request import ScrapeRequest
from app.services.audio_service import AudioService
from app.services.captcha_solver import CaptchaSolver
from app.services.scraper_service import ScraperService
from playwright.sync_api import sync_playwright

app = FastAPI()

@app.post("/scrape")
def scrape(request: ScrapeRequest):
    try:
        audio_service = AudioService()
        captcha_solver = CaptchaSolver(audio_service)
        scraper_service = ScraperService(captcha_solver)
        
        with sync_playwright() as playwright:
            content = scraper_service.scrape(playwright, request.url)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
