.PHONY: init tests docs build clean

init:
	pip install -r requirements.txt

tests:
	python scripts/tests.py

docs:
	python scripts/docs.py

build:
	python setup.py sdist bdist_wheel

clean:
	python scripts/clean.py
