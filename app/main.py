from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.schemas.scrape_request import ScrapeRequest
from app.services.scraper_service import ScraperService
from app.container import container

app = FastAPI()


@app.post("/scrape")
def scrape(request: ScrapeRequest):
    scraper_service: ScraperService = container[ScraperService]
    try:
        content = scraper_service.scrape(request.url)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
