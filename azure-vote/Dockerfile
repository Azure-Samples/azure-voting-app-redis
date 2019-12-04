FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install redis
ADD /azure-vote /app
RUN chmod 755 /app /app/static && chmod 644 /app/static/*

