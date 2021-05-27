.PHONY: install test flake8 black isort

install:
	venv/bin/pip install -Ur requirements.txt

test: tests
	pytest tests

flake8: venv/bin/flake8 # Lints code using flake8
	venv/bin/flake8 src

black: venv/bin/black # Formats code with black
	venv/bin/black src

isort: venv/bin/isort # Sorts imports using isort
	venv/bin/isort src

# Optional if you need jupyter notebook
project_name = structure

jupyter: venv/bin/ipython
	venv/bin/jupyter notebook

venv/bin/ipython:
	venv/bin/pip install -U ipykernel jupyter
	venv/bin/ipython kernel install --user --name=$(project_name)