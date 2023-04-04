# Useful commands

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

```
docker-compose exec web python -m pytest -p no:warnings
```

run only the last failed tests

```
docker-compose exec web python -m pytest --lf
```

run only the tests with names that match the string expression

```
docker-compose exec web python -m pytest -k "summary and not test_read_summary"
```

stop the test session after the first failure

```
docker-compose exec web python -m pytest -x
```

enter PDB after first failure then end the test session

```
docker-compose exec web python -m pytest -x --pdb
```

stop the test run after two failures

```
docker-compose exec web python -m pytest --maxfail=2
```

show local variables in tracebacks

```
docker-compose exec web python -m pytest -l
```

list the 2 slowest tests

```
docker-compose exec web python -m pytest --durations=2
```
