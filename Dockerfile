FROM docker.io/python:3.10-alpine3.16
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
