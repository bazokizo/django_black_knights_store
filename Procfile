web: gunicorn myshop.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py migrate