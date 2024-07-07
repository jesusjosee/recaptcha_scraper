FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala Playwright y  navegadores
RUN apt-get update && apt-get install -y wget unzip curl libgtk-3-0 libgbm1 libnss3 libasound2 fonts-noto-color-emoji
RUN playwright install


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
