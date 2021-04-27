import json
import uuid

import pika
import logging

from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage


class RadioPlayerRpcClient:
    def __init__(self):
        self.logger = logging.getLogger('radio_player')

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='radio-player-rpc', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        message = RadioPlayerRpcMessage.from_json(json.loads(body))
        return message

    def call(self, request):
        try:
            request_data = json.dumps(request, default=lambda o: o.__dict__)
            self.logger.debug(f'send message to player: {request_data}')

            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='',
                routing_key='rpc_queue',
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=str(request_data))
            while self.response is None:
                self.connection.process_data_events()
            return self.response
        except:
            self.logger.error(f'could not send {request_data}')
            raise
