.PHONY: clean-pyc

help:
	@echo "clean - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "format - format with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "see-coverage - run python http.server in htmlcov"
	@echo "migrations - generate the new migrations"
	@echo "migrate - persist the migrations"
	@echo "run-dev - run in development mode [local]"
	@echo "run-dev - run in development mode [test]"
	@echo "run-dev - run in development mode [prod]"
	@echo "run-docker - run in development mode [docker instance]"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf .tox +
	rm -rf .pytest_cache

lint:
	flake8 market ieb_service_http tests

format:
	black market ieb_service_http tests

test:
	tox

see-coverage:
	python -m http.server --directory=htmlcov/

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver

run-dev:
	 python manage.py runserver --settings=ieb_service_http.settings.development

run-test:
	 python manage.py runserver --settings=ieb_service_http.settings.test

run-prod:
	 python manage.py runserver --settings=ieb_service_http.settings.production

run-docker:
	docker-compose up -d