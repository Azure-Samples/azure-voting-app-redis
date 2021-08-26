FROM    tiangolo/uwsgi-nginx-flask:python3.6

COPY sshd_config /etc/ssh/
COPY app_init.supervisord.conf /etc/supervisor/conf.d

RUN  mkdir -p /home/LogFiles \
     && echo "root:Docker!" | chpasswd \
     && echo "cd /home" >> /etc/bash.bashrc \
     && apt update \
     && apt install -y --no-install-recommends openssh-server vim curl wget tcptraceroute

RUN  pip install redis

EXPOSE 2222 80
 
ADD     /azure-vote /app

ENV PORT 80
ENV PATH ${PATH}:/home/site/wwwroot

# Supervisor will call into /opt/startup/init_container.sh
# Also see: http://blog.trifork.com/2014/03/11/using-supervisor-with-docker-to-manage-processes-supporting-image-inheritance/
CMD ["/usr/bin/supervisord"]
