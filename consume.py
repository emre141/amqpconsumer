"""Basic message consumer example"""
import functools
import logging
import pika
import os


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)

amqpuser = os.environ['amqpuser']
amqppassword = os.environ['amqppassword']
amqphost = os.environ['amqphost']
queue = os.environ['queue']
routing_key = os.environ['routingkey']
exchange = os.environ['exchange']

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def on_message(chan, method_frame, _header_frame, body, userdata=None):
    """Called when a message is received. Log message and ack it."""
    LOGGER.info('Userdata: %s Message body: %s', userdata, body)
    chan.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():
    """Main method."""
    credentials = pika.PlainCredentials(amqpuser,amqppassword )
    parameters = pika.ConnectionParameters(amqphost, credentials=credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    res = channel.queue_declare(queue=queue, auto_delete=True)
    channel.queue_bind(
        queue=queue, exchange=exchange, routing_key=routing_key)
    channel.basic_qos(prefetch_count=10)
    print('Messages in queue %d' % res.method.message_count)

    on_message_callback = functools.partial(
        on_message, userdata='on_message_userdata')
    channel.basic_consume(queue, on_message_callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
    print('Messages in queue %d' % res.method.message_count)


if __name__ == '__main__':
    main()

