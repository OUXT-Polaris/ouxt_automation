FROM ghcr.io/astral-sh/uv:python3.10-alpine

WORKDIR /app
COPY mqtt_endpoint .
RUN uv sync
# RUN uv run main.py
CMD ["/bin/sh"]
# CMD ["uv sync"]
