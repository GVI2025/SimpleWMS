all: install makemigrations migrate seed run

install:
    poetry install

migrate:
    poetry run alembic upgrade head

makemigrations:
    poetry run alembic revision --autogenerate

seed:
    poetry run python -m app.seed.seed_data

run:
    poetry run uvicorn app.main:app --reload

test:
    poetry run test

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf .pytest_cache