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

Run tests

```bash
docker-compose exec web python -m pytest
```
