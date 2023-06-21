.PHONY: pip
pip:
	python3 setup.py sdist

.PHONY: clean
clean:
	rm -rf dist \
		joyeuse.egg-info \
		`find -name __pycache__` \
		`find -name '*.pyc'`
