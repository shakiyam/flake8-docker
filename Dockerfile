FROM container-registry.oracle.com/os/oraclelinux:9-slim
# hadolint ignore=DL3041
RUN microdnf -y install python3 pip \
  && microdnf clean all \
  && rm -rf /var/cache
COPY requirements.txt /requirements.txt
# hadolint ignore=DL3013
RUN python3 -m pip install --no-cache-dir --upgrade pip && python3 -m pip install --no-cache-dir -r /requirements.txt
WORKDIR /work
ENTRYPOINT ["flake8"]
