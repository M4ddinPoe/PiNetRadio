import json
import unittest

from src.Messages.InfoRequest import InfoRequest
from src.Messages.InfoResponse import InfoResponse
from src.Messages.PlayRequest import PlayRequest
from src.Messages.PlayResponse import PlayResponse
from src.Messages.RadioPlayerRpcMessage import RadioPlayerRpcMessage
from src.Messages.RadiosRequest import RadiosRequest
from src.Messages.RadiosResponse import RadiosResponse
from src.Player.Core.Model.PlayerInfo import PlayerInfo
from src.Player.Core.Model.Radio import Radio


class TestRadioPlayerRpcMessageSerialization(unittest.TestCase):

    def test_serialize_play_request(self):
        expected = '{"data_type": "PlayRequest", "data": {"id": 1}}'
        message_data = PlayRequest(1)

        self._execute_serialize_test(expected, message_data)

    def test_deserialize_play_request(self):
        serialized = '{"data_type": "PlayRequest", "data": {"id": 1}}'
        self._execute_deserialize_test(serialized, PlayRequest)

    def test_serialize_play_response(self):
        expected = '{"data_type": "PlayResponse", "data": {"success": true, "error": ""}}'
        message_data = PlayResponse()

        self._execute_serialize_test(expected, message_data)

    def test_deserialize_play_response(self):
        serialized = '{"data_type": "PlayResponse", "data": {"success": true, "error": ""}}'
        self._execute_deserialize_test(serialized, PlayResponse)

    def test_serialize_radios_request(self):
        expected = '{"data_type": "RadiosRequest", "data": {}}'
        message_data = RadiosRequest()

        self._execute_serialize_test(expected, message_data)

    def test_deserialize_radios_request(self):
        serialized = '{"data_type": "RadiosRequest", "data": {}}'
        self._execute_deserialize_test(serialized, RadiosRequest)

    def test_serialize_radios_response(self):
        expected = '{"data_type": "RadiosResponse", "data": {"radios": [{"id": 1, "title": "Radio 1", "url": "http://radio1.loc"}, {"id": 2, "title": "Radio 2", "url": "http://radio2.loc"}]}}'
        message_data = RadiosResponse(
            [Radio(1, 'Radio 1', 'http://radio1.loc'), Radio(2, 'Radio 2', 'http://radio2.loc')])

        self._execute_serialize_test(expected, message_data)

    def test_deserialize_radios_response(self):
        serialized = '{"data_type": "RadiosResponse", "data": {"radios": [{"id": 1, "title": "Radio 1", "url": "http://radio1.loc"}, {"id": 2, "title": "Radio 2", "url": "http://radio2.loc"}]}}'
        self._execute_deserialize_test(serialized, RadiosResponse)

    def test_serialize_infos_request(self):
        expected = '{"data_type": "InfoRequest", "data": {}}'
        message_data = InfoRequest()

        self._execute_serialize_test(expected, message_data)

    def test_deserialize_infos_request(self):
        serialized = '{"data_type": "InfoRequest", "data": {}}'
        self._execute_deserialize_test(serialized, InfoRequest)

    def test_serialize_infos_response(self):
        expected = '{"data_type": "InfoResponse", "data": {"info": {"volume": 50, "radio": {"id": 1, "title": "Radio 1", "url": "http://radio1.loc"}, "status": "stopped"}}}'
        message_data = InfoResponse(
            PlayerInfo(Radio(1, 'Radio 1', 'http://radio1.loc'), 50, "stopped"))

        self._execute_serialize_test(expected, message_data)

    def _execute_serialize_test(self, expected_json, message_data_object):
        message = RadioPlayerRpcMessage(data=message_data_object)

        data = json.dumps(message, default=lambda o: o.__dict__)

        self.assertEqual(expected_json, data)

    def _execute_deserialize_test(self, serialized_json, message_data_type):
        message_data_type_name = message_data_type.__name__

        loaded_json = json.loads(serialized_json)
        decoded_message = RadioPlayerRpcMessage.from_json(loaded_json)

        self.assertEqual(message_data_type_name, decoded_message.data_type)
        self.assertTrue(isinstance(decoded_message.data, message_data_type))

if __name__ == '__main__':
    unittest.main()
