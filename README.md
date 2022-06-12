# Porfolio - Elias Guere

Este proyecto tiene como objetivo presentar mi perfil como programador y mis proyectos. Esta desarrollado en Django v3.*.

## Requerimientos
- Docker y docker compose v3.9 (opcional)
- PostgreSQL v12.6
- Python v3.*

## Deploy

Si tienes docker y docker-compose:
```
    # Construir y desplegar el proyecto
    docker-compose up -d --build

    # Para cargar los datos por defecto
    docker-compose exec web python manage.py loaddata ./data/data.json
```
