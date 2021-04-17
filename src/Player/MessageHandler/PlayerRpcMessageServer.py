import pika
import logging
import json

from src.Messages.ChangeVolumeResponse import ChangeVolumeResponse
from src.Messages.InfoResponse import InfoResponse
from src.Messages.PlayResponse import PlayResponse
from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage
from src.Messages.RadiosResponse import RadiosResponse
from src.Messages.StopResponse import StopResponse
from src.Player.Core.RadioPlayer import RadioPlayer


class ShutdownResonse:
    pass


class PlayerRpcMessageServer:

    def __init__(self):
        self.handler_map = {
            'PlayRequest': self._handle_play_request,
            'RadiosRequest': self._handle_radios_request,
            'StopRequest': self._handle_stop_request,
            'ChangeVolumeRequest': self._handle_change_volume_request,
            'InfoRequest': self._handle_info_request,
            'ShutdownRequest': self._handle_shutdown_request,
        }

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

        message = RadioPlayerRpcMessage.from_json(json.loads(body))

        response = self.handler_map[message.data_type](message.data)
        response_data = json.dumps(response, default=lambda o: o.__dict__)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=str(response_data))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def _handle_play_request(self, play_request):
        self.player.play(play_request.id)
        return PlayResponse()

    def _handle_radios_request(self, radios_request):
        radios = self.player.get_radios()
        return RadiosResponse(radios)

    def _handle_stop_request(self, stop_request):
        self.player.stop()
        return StopResponse()

    def _handle_change_volume_request(self, change_volume_request):
        self.player.set_volume(change_volume_request.volume)
        return ChangeVolumeResponse()

    def _handle_info_request(self, info_request):
        info = self.player.get_info()
        return InfoResponse(info)

    def _handle_shutdown_request(self, shutdown):
        self.player.shutdown()
        return ShutdownResonse()