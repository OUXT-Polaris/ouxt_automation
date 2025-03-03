FROM ghcr.io/astral-sh/uv:python3.10-alpine

WORKDIR /app
COPY mqtt_endpoint .
RUN uv sync
CMD ["uv", "run", "endpoint"]
