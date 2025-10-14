FROM python:3.14-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY requirements.txt /requirements.txt
RUN uv pip install --system --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
