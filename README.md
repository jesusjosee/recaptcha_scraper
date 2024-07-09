# ReCaptcha Scraper

## Descripción

Esta aplicación realiza scraping en sitios web protegidos por ReCaptcha utilizando Playwright y expone una API REST con FastAPI.

## Requisitos

- Docker
- Docker Compose

## Instrucciones de Uso


1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/jesusjosee/recaptcha_scraper.git
   cd recaptcha_scraper
   ```

### Levantar el servicio:

```bash
docker compose up --build
```

### Ejecutar tests:

```bash
docker-compose run test
```
## API

### Endpoint: `/scrape`

- **Método:** POST
- **Body:** JSON

### Ejemplo de solicitud

```bash
curl -X POST "http://localhost:8000/scrape" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com/recaptcha/api2/demo"}'

{
  "content": "Contenido protegido por captcha o resolución del captcha"
}

```