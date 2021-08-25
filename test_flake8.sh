#!/bin/bash
set -eu -o pipefail

docker container run \
  --name test_flake8$$ \
  --rm \
  -u "$(id -u):$(id -g)" \
  -v "$PWD":/work:ro \
  --entrypoint python3 \
  shakiyam/flake8 ./test/test_flake8.py
