FROM ghcr.io/astral-sh/uv:python3.10-alpine

WORKDIR /app
COPY udp_forwarder .
RUN uv sync
# CMD ["uv", "run", "endpoint"]
