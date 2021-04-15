import json


#class RadioPlayerRpcMessageEncoder(json.JSONEncoder):
#    def __int__(self):
#        self.type = {RadioPlayerRpcMessage: self.show_radios,
#                         'play': self.play,
#                         'stop': self.stop,
#                         'volume': self.set_volume,
#                         'info': self.show_info}
#
#    def default(self, z):
#        if isinstance(z, complex):
#            return (z.real, z.imag)
#        else:
#            return super().default(z)



class RadioPlayerRpcMessage:
    def __init__(self, message):
        data_type = type(message).__name__
        data = message

class PlayRequest:
    def __init__(self, url):
        self.url = url

class PlayRequest:
    def __init__(self, url):
        self.url = url

class RadiosRequest:
    pass

class RadiosResponse:
    radios = []

class StopRequest:
    pass

class StopResponse:
    pass

class ChangeVolumeRequest:
    volume = 0
    pass

class ChangeVolumeResponse:
    current_volume = 0
    pass

class InfoRequest:
    pass

class InfoResponse:
    info = {}
    pass

class ShutdownRequest:
    pass

class ShutdownResponse:
    pass

