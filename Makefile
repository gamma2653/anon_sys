

build: build_python build_rust

build_python:
	cd python/
	source venv/bin/activate && python -m build .
