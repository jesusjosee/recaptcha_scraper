FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala Playwright, navegadores y dependencias necesarias en una sola capa
RUN apt-get update && \
    apt-get install -y wget unzip curl libgtk-3-0 libgbm1 libnss3 libasound2 fonts-noto-color-emoji portaudio19-dev ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN playwright install

COPY . .

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
