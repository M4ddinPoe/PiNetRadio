import pika
import json
import logging
from src.Player.Core.RadioPlayer import RadioPlayer

class PlayHandler:
    def __init__(self):
        self.logger = logging.getLogger('radio_player')
        self.logger.info('initializing play handle')
        self.player = RadioPlayer()

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='radio-player', exchange_type='fanout')

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue

        self.channel.queue_bind(exchange='radio-player', queue=self.queue_name)

        self.logger.info(' [*] Waiting for commands.')
        print('To exit press CTRL+C')

    def callback(self, ch, method, properties, body):
        try:
            self.logger.info('received message')
            self.logger.debug(" [x] %r" % body)

            playMessage = json.loads(body)

            if playMessage['command'] == 'play':
                self.logger.info(f" [..] player.start: {str(playMessage['data'])}")
                self.player.play(playMessage['data'])
            elif playMessage['command'] == 'stop':
                self.logger.info(f" [..] player.stop")
                self.player.stop()
            elif playMessage['command'] == 'volume':
                self.logger.info(f" [..] player.volume: {str(playMessage['data'])}")
                volume = int(playMessage['data'])
                self.player.set_volume(volume)
            elif playMessage['command'] == 'info':
                self.logger.info(f" [..] player.info")
                info = self.player.get_info()

                ch.basic_publish(exchange='',
                                 routing_key=props.reply_to,
                                 properties=pika.BasicProperties(correlation_id=props.correlation_id),
                                 body=info
                                 )

                ch.basic_ack(delivery_tag=method.delivery_tag)

            elif playMessage['command'] == 'shutdown':
                self.logger.info(f" [..] system.shutdown")
                self.player.shutdown()
        except:
            logging.error('could not execute command')

    def start(self):
        try:
            self.logger.info('player started')
            self.channel.basic_consume(
                queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

            self.channel.start_consuming()
        except:
            self.logger.error('unable to start player')