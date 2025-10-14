FROM python:3.14-slim-bookworm
COPY requirements.txt /requirements.txt
# hadolint ignore=DL3013
RUN python3 -m pip install --no-cache-dir --upgrade pip && python3 -m pip install --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
