build:
	python setup.py sdist bdist_wheel

test-upload:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python -m twine upload dist/*
