#!/usr/bin/env bash
# Ejecuta migraciones y recolecta archivos estáticos automáticamente
python manage.py migrate
python manage.py collectstatic --noinput
