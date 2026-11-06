install:
	uv sync

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff tests

lint-fix:
	uv run ruff check gendiff tests --fix --unsafe-fixes

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml
