FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.9.9 /uv /bin/uv
COPY requirements.txt /requirements.txt
RUN uv pip install --system --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
