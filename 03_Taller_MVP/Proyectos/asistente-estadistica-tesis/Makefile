.PHONY: install test lint format run clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

lint:
	python -m ruff check src tests

format:
	python -m ruff format src tests

run:
	python -m uvicorn src.main:app --reload

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
