ARG PYTHON_VERSION=3.13
ARG HEAVY_BUILD

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

RUN if [ "$HEAVY_BUILD" = "true" ]; then python -c "from main import heavy_calculation; print(f'Pre-calculating {heavy_calculation()} prime numbers...')"; fi
