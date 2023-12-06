# Variables
POETRY = poetry


install:
	$(POETRY) install --no-root
	$(POETRY) run pre-commit install

format:
	$(POETRY) run black .

lint:
	$(POETRY) run pflake8

typecheck:
	$(POETRY) run mypy ./src

test:
	$(POETRY) run pytest tests/ --cov=src --cov-report=term

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +

build:
	$(POETRY) build

# Docker Compose commands
compose-build:
	@docker compose build

compose-up:
	@docker compose up -d

compose-down:
	@docker compose down -t 0

compose-logs:
	@docker compose logs -f

compose-migration:
	@docker compose run --rm app sh -c "cd src/infrastructure/ && alembic revision --autogenerate -m $(MESSAGE)"

compose-upgrade:
	@docker compose run --rm app sh -c "cd src/infrastructure/ && alembic upgrade head"

compose-downgrade:
	@docker compose run --rm app sh -c "cd src/infrastructure/ && alembic downgrade -1"