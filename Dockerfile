FROM python:3.10-alpine
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
