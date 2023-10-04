#!/bin/sh

set -e

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput

# Start the Django development server
gunicorn mlw.wsgi:application --bind :8000