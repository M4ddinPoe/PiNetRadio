import unittest

from src.Messages.ChangeVolumeRequest import ChangeVolumeRequest
from src.Messages.ChangeVolumeResponse import ChangeVolumeResponse
from src.Messages.InfoRequest import InfoRequest
from src.Messages.InfoResponse import InfoResponse
from src.Messages.PlayRequest import PlayRequest
from src.Messages.PlayResponse import PlayResponse
from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage
from src.Messages.RadiosRequest import RadiosRequest
from src.Messages.RadiosResponse import RadiosResponse
from src.Messages.ShutdownRequest import ShutdownRequest
from src.Messages.ShutdownResponse import ShutdownResponse
from src.Messages.StopRequest import StopRequest
from src.Messages.StopResponse import StopResponse
from src.Player.Core.Model.Radio import Radio
from src.Player.MessageHandler.PlayerMessageHandler import PlayerRpcMessageServer


class RpcMessageServerMock:
    def start(self, handler):
        self.handler = handler

    def invoke(self, request):
        self.handler(request)


class PlayerMock:
    def get_radios(self):
        return [Radio(1, 'Radion 1', 'http://radio1.loc'), Radio(2, 'Radion 2', 'http://radio2.loc')]

    def play(self, id):
        pass

    def stop(self):
        pass

    def set_volume(self, volume):
        pass

    def get_info(self):
        pass

    def shutdown(self):
        pass

class TestPlayerMessageHandler(unittest.TestCase):
    def setUp(self):
        self.rpc_message_server_mock = RpcMessageServerMock()
        player = PlayerMock()

        self.server = PlayerRpcMessageServer(self.rpc_message_server_mock, player)

    def test_play_request(self):
        request = PlayRequest(1)
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, PlayResponse))

    def test_stop_request(self):
        request = StopRequest()
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, StopResponse))

    def test_radios_request(self):
        request = RadiosRequest()
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, RadiosResponse))

    def test_change_volume_request(self):
        request = ChangeVolumeRequest(50)
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, ChangeVolumeResponse))

    def test_info_request(self):
        request = InfoRequest()
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, InfoResponse))

    def test_shutdown_request(self):
        request = ShutdownRequest()
        rpc_message = RadioPlayerRpcMessage(request)

        response = self.server.handle_message(rpc_message)

        self.assertTrue(isinstance(response, ShutdownResponse))

if __name__ == '__main__':
    unittest.main()