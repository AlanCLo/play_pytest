.PHONY: test pep8


test:
	python -m pytest -v

test_add:
	python -m pytest -v -k add

test_set1:
	python -m pytest -v -m set1

pep8:
	python -m pytest --pep8
