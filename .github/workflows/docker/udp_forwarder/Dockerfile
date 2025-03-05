FROM ghcr.io/astral-sh/uv:python3.10-alpine

RUN apk update && apk add --no-cache \
    build-base \
    pkgconfig \
    sdl2-dev \
    freetype-dev \
    python3-dev

WORKDIR /app
COPY udp_forwarder .
RUN uv sync
# CMD ["uv", "run", "endpoint"]
