FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install redis numpy
RUN echo "uwsgi_read_timeout 300s;" > /etc/nginx/conf.d/custom_timeout.conf
ADD /azure-vote /app
