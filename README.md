# acr_test

To run tests, you have to run virtual environment for this repository.

### Running venv

Set python version for repo and set venv and activate.
```sh
$ pyenv install 3.12.7
$ pyenv local 3.12.7
$ python -m venv env
$ source env/bin/activate
```

### Install python dependencies in repo directory
```sh
pip install -U setuptools pip
pip install -e .
```

### Run tests
```sh
$ pytest -sv
```

tools  - directory with tasks source code

test - directory with tests
