import logging

from src.Messages.ChangeVolumeResponse import ChangeVolumeResponse
from src.Messages.InfoResponse import InfoResponse
from src.Messages.PlayResponse import PlayResponse
from src.Messages.RadiosResponse import RadiosResponse
from src.Messages.ShutdownResponse import ShutdownResponse
from src.Messages.StopResponse import StopResponse


class PlayerMessageHandler:

    def __init__(self, rpc_message_server, player):
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
        self.player = player

        self.logger.info(' [*] Waiting for commands.')
        rpc_message_server.start(self.handle_message)
        self.logger.info(" [x] Awaiting RPC requests")
        print('To exit press CTRL+C')

    def handle_message(self, request):
        response = self.handler_map[request.data_type](request.data)
        return response

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
        return ShutdownResponse()