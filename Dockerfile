FROM python:3.14-slim AS builder

WORKDIR /app

COPY src/ /app/src

RUN python3 src/generator.py

FROM joseluisq/static-web-server

COPY --from=builder /app/public/ /public

ENV SERVER_CACHE_CONTROL_HEADERS=false
