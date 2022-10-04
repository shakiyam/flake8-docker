#!/bin/bash
set -eu -o pipefail

if [[ $(command -v docker) ]]; then
  docker container run \
    --entrypoint python3 \
    --name test_flake8$$ \
    --rm \
    -u "$(id -u):$(id -g)" \
    -v "$PWD":/work:ro \
    docker.io/shakiyam/flake8 ./test/test_flake8.py
elif [[ $(command -v podman) ]]; then
  podman container run \
    --entrypoint python3 \
    --name test_flake8$$ \
    --rm \
    --security-opt label=disable \
    -v "$PWD":/work:ro \
    docker.io/shakiyam/flake8 ./test/test_flake8.py "$@"
else
  echo "Neither docker nor podman is installed."
  exit 1
fi
