ARG PYTHON_VERSION=3.13
ARG HEAVY_BUILD=false

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

COPY main.py .

# Pass ARG to ENV so it survives into RUN layer
ARG HEAVY_BUILD
ENV HEAVY_BUILD=${HEAVY_BUILD}

RUN echo "HEAVY_BUILD=$HEAVY_BUILD" && \
    if [ "$HEAVY_BUILD" = "true" ]; then \
        python -c "from main import heavy_calculation; print(f'Pre-calculating {heavy_calculation()} prime numbers...')"; \
    fi