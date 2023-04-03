# FROM tiangolo/uwsgi-nginx-flask:python3.6

# Update the base image to use Python 3.11
FROM tiangolo/uwsgi-nginx:python3.11
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.

ENV PYTHONPATH=/app



RUN pip install redis
ADD /azure-vote /app
