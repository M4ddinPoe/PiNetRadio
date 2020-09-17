import pika
import json
from src.Player.Core.RadioPlayer import RadioPlayer

class PlayHandler:
    def __init__(self):
        self.player = RadioPlayer()

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='radio-player', exchange_type='fanout')

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue

        self.channel.queue_bind(exchange='radio-player', queue=self.queue_name)

        print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)

        playMessage = json.loads(body)

        if playMessage['command'] == 'play':
            print(" [..] player.start: %s" % playMessage['url'])
            self.player.play(playMessage['url'])
        elif playMessage['command'] == 'stop':
            print(" [..] player.stop")
            self.player.stop()
        elif playMessage['command'] == 'volume':
            print(" [..] player.volume: %i" %playMessage['volume'])
            self.player.set_volume(playMessage['volume'])

    def start(self):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        self.channel.start_consuming()