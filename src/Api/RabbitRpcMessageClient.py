import json
import uuid

import pika

from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage


class RabbitRpcMessageClient(object):
    def __init__(self, host, queue_name):
        self.queue_name = queue_name

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            message = RadioPlayerRpcMessage.from_json(json.loads(body))
            self.response = message.data

    def call(self, request):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        message = RadioPlayerRpcMessage(data=request)
        data = json.dumps(message, default=lambda o: o.__dict__)

        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=data)
        while self.response is None:
            self.connection.process_data_events()
        return self.response
