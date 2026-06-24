.PHONY: help run migrate check test shell css watch-css docker-up docker-build clean

help:
	@echo "B-Commerce Makefile"
	@echo ""
	@echo "Uso:"
	@echo "  make run         Iniciar servidor de desarrollo"
	@echo "  make migrate     Ejecutar migraciones"
	@echo "  make check       Validar proyecto Django"
	@echo "  make test        Ejecutar tests"
	@echo "  make shell       Abrir shell de Django"
	@echo "  make css         Compilar Tailwind CSS"
	@echo "  make watch-css   Compilar Tailwind en modo watch"
	@echo "  make docker-up   Iniciar con Docker Compose"
	@echo "  make docker-build Construir imágenes Docker"
	@echo "  make clean       Limpiar archivos generados"

run:
	python manage.py runserver

migrate:
	python manage.py migrate

check:
	python manage.py check --deploy

test:
	python -m pytest tests/ --ds=config.settings.test -v

shell:
	python manage.py shell

css:
	npm run build:css

watch-css:
	npm run watch:css

docker-up:
	docker compose up --build

docker-build:
	docker compose build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .pytest_cache htmlcov .coverage
