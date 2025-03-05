FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libsdl2-dev \
    libfreetype6-dev

WORKDIR /app
COPY mqtt_endpoint .
RUN pip install --no-cache-dir -r requirements.txt #requirements.txtがある場合
CMD ["python", "endpoint.py"] #endpoint.pyがある場合
