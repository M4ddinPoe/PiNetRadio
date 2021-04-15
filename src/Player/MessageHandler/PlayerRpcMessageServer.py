import pika
import logging
import json

from src.Player.Core.RadioPlayer import RadioPlayer


class PlayerRpcMessageServer:

    def __init__(self):
        self.logger = logging.getLogger('radio_player')
        self.logger.info('initializing play handle')
        self.player = RadioPlayer()

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = connection.channel()
        self.channel.queue_declare(queue='radio_player_rpc_queue')

        self.logger.info(' [*] Waiting for commands.')
        print('To exit press CTRL+C')

    def start(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='radio_player_rpc_queue', on_message_callback=self.handle_message())

        self.logger.info(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def handle_message(self, ch, method, props, body):
        self.logger.info('received message')
        self.logger.debug(" [x] %r" % body)

        playMessage = json.loads(body)


