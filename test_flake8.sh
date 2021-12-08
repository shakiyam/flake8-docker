#!/bin/bash
set -eu -o pipefail

if [[ $(command -v podman) ]]; then
  podman container run \
    --name test_flake8$$ \
    --rm \
    --security-opt label=disable \
    -v "$PWD":/work:ro \
    --entrypoint python3 \
    shakiyam/flake8 ./test/test_flake8.py "$@"
else
  docker container run \
    --name test_flake8$$ \
    --rm \
    -u "$(id -u):$(id -g)" \
    -v "$PWD":/work:ro \
    --entrypoint python3 \
    shakiyam/flake8 ./test/test_flake8.py
fi
