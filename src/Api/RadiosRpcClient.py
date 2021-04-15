import pika
import logging

class RadioPlayerRpcClient:
    def __init__(self):
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
        #todo: unpack json
        return []

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

def send_message(command, data):
    try:
        logger = logging.getLogger('radio_player')
        logger.debug(f'try send {command} command with data: {data}')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='radio-player', exchange_type='fanout')

        message = '{ "command":"%s", "data": "%s" }' %(command, str(data))
        channel.basic_publish(exchange='radio-player', routing_key='', body=message)
        print(" [x] Sent %r" % message)
        connection.close()
    except:
        logger.error(f'cloud not send {command} command with data: {data}')