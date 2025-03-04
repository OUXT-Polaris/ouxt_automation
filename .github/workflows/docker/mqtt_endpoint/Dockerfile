FROM ghcr.io/astral-sh/uv:python3.10-alpine

RUN apk update && apk add --no-cache \
    build-base \
    pkgconfig \
    sdl2-dev \
    freetype-dev \
    python3-dev

WORKDIR /app
COPY mqtt_endpoint .
RUN uv sync
CMD ["uv", "run", "endpoint"]
