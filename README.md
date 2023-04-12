# Test-Driven Development with FastAPI and Docker

![CI/CD](https://github.com/chri55c/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)

https://testdriven.io/courses/tdd-fastapi/

## Main changes from course

- Removed `project` folder and moved contents of it to root folder (seems nicer to me)
- Using poetry for dependency management


## Useful commands


Spin up containers

```bash
docker-compose up -d
```

Spin up and build containers

```bash
docker-compose up -d --build
```

View logs

```bash
docker-compose logs -f
```

View logs of a specific container

```bash
docker-compose logs -f <container_name>
```

Access PostgreSQL database

```bash
docker-compose exec web-db psql -U postgres
```

Spin down containers

```bash
docker-compose down
```

Spin down and remove containers

```bash
docker-compose down --rmi all
```

Spin down and remove containers and volumes

```bash
docker-compose down --rmi all -v
```

Spin down and remove containers and volumes and networks

```bash
docker-compose down --rmi all -v --remove-orphans
```

Change permissions of a file

```bash
chmod +x <file_name>
```

## Database

Initialise Aerich

```bash
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
```

Create first migration

```bash
docker-compose exec web aerich init-db
```

Migrate database

```bash
docker-compose exec web aerich migrate
```

Upgrade database

```bash
docker-compose exec web aerich upgrade
```

Generate schema (skip migrations)

```bash
docker-compose exec web python app/db.py
```

## Tests

```bash
docker-compose exec web python -m pytest
```

disable warnings

```bash
docker-compose exec web python -m pytest -p no:warnings
```

run only the last failed tests

```bash
docker-compose exec web python -m pytest --lf
```

run only the tests with names that match the string expression

```bash
docker-compose exec web python -m pytest -k "summary and not test_read_summary"
```

stop the test session after the first failure

```bash
docker-compose exec web python -m pytest -x
```

enter PDB after first failure then end the test session

```bash
docker-compose exec web python -m pytest -x --pdb
```

stop the test run after two failures

```bash
docker-compose exec web python -m pytest --maxfail=2
```

show local variables in tracebacks

```bash
docker-compose exec web python -m pytest -l
```

list the 2 slowest tests

```bash
docker-compose exec web python -m pytest --durations=2
```

run tests in parallel (requires `pytest-xdist`)
```bash
docker-compose exec web pytest -n auto
```

## Package management

Login to GitHub Container Registry

```bash
docker login ghcr.io -u <USERNAME> -p <TOKEN>
```

Build prod image
```bash
docker build -f Dockerfile.prod -t ghcr.io/chri55c/fastapi-tdd-docker/summarizer:latest .
```

Push prod image
```bash
docker push ghcr.io/chri55c/fastapi-tdd-docker/summarizer:latest
```
