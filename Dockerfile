FROM python:3

ARG proxy_host
ARG proxy_port

COPY setup-proxy.sh /tmp/setup-proxy.sh
COPY consume.py consume.py

RUN . /tmp/setup-proxy.sh && \
    pip  install pika

CMD ["python", "consume.py"]

