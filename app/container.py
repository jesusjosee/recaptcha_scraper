from lagom import Container
from app.services.scraper_service import ScraperService
from app.resolvers.recaptcha_v2_checkbox_resolver import RecaptchaV2CheckboxResolver

container = Container()
container[ScraperService] = ScraperService(container[RecaptchaV2CheckboxResolver])
