import json

import pika

from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage


class RabbitRpcMessageServer:
    def __init__(self, host, queue_name):
        self.queue_name = queue_name

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))

        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def start(self, message_handler):
        self.message_handler = message_handler
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.handle_message)

        self.channel.start_consuming()

    def handle_message(self, ch, method, props, body):
        message = RadioPlayerRpcMessage.from_json(json.loads(body))

        response = self.message_handler(message)

        message = RadioPlayerRpcMessage(data=response)
        response_data = json.dumps(message, default=lambda o: o.__dict__)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response_data)
        ch.basic_ack(delivery_tag=method.delivery_tag)