from src.Messages.ChangeVolumeRequest import ChangeVolumeRequest
from src.Messages.ChangeVolumeResponse import ChangeVolumeResponse
from src.Messages.InfoRequest import InfoRequest
from src.Messages.InfoResponse import InfoResponse
from src.Messages.PlayRequest import PlayRequest
from src.Messages.PlayResponse import PlayResponse
from src.Messages.RadiosRequest import RadiosRequest
from src.Messages.RadiosResponse import RadiosResponse
from src.Messages.ShutdownRequest import ShutdownRequest
from src.Messages.ShutdownResponse import ShutdownResponse
from src.Messages.StopRequest import StopRequest
from src.Messages.StopResponse import StopResponse

data_type_map = {
    'PlayRequest': PlayRequest.from_json,
    'PlayResponse': PlayResponse.from_json,
    'RadiosRequest': RadiosRequest.from_json,
    'RadiosResponse': RadiosResponse.from_json,
    'StopRequest': StopRequest.from_json,
    'StopResponse': StopResponse.from_json,
    'ChangeVolumeRequest': ChangeVolumeRequest.from_json,
    'ChangeVolumeResponse': ChangeVolumeResponse.from_json,
    'InfoRequest': InfoRequest.from_json,
    'InfoResponse': InfoResponse.from_json,
    'ShutdownRequest': ShutdownRequest.from_json,
    'ShutdownResponse': ShutdownResponse.from_json
}

class RadioPlayerRpcMessage:
    def __init__(self, data):
        self.data_type = type(data).__name__
        self.data = data

    @classmethod
    def from_json(cls, dictionary):
        data_type = dictionary['data_type']
        data_dictionary = dictionary['data']

        seralizerMethod = data_type_map[data_type]
        data = seralizerMethod(data_dictionary)

        return cls(data)