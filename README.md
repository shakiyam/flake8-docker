flake8-docker
=============

> [!WARNING]
> This project is archived and no longer maintained.
> Consider using [Ruff](https://github.com/astral-sh/ruff) instead, which is significantly faster and replaces flake8 and many of its plugins.
> Official Docker image is available at [ghcr.io/astral-sh/ruff](https://github.com/astral-sh/ruff/pkgs/container/ruff).

[Flake8](https://pypi.org/project/flake8/) Docker Image

The following plugins have been installed.

* [flake8-builtins](https://pypi.org/project/flake8-builtins/)
* [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/)
* [flake8-import-order](https://pypi.org/project/flake8-import-order/)
* [flake8-quotes](https://pypi.org/project/flake8-quotes/)
* [flake8-use-fstring](https://pypi.org/project/flake8-use-fstring/)
* [pep8-naming](https://pypi.org/project/pep8-naming/)

Installation
------------

```console
curl -L# https://raw.githubusercontent.com/shakiyam/flake8-docker/main/flake8 \
  | sudo tee /usr/local/bin/flake8 >/dev/null
sudo chmod +x /usr/local/bin/flake8
```

Usage
-----

To get help with the command line:

```console
flake8 --help
```

For detailed documentation of Flake8, see [here](https://flake8.pycqa.org/en/latest/).

Author
------

[Shinichi Akiyama](https://github.com/shakiyam)

License
-------

[MIT License](https://opensource.org/licenses/MIT)
