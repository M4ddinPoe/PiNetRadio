from src.Messages.MessageData import MessageData


class RadiosResponse(MessageData):
    def __init__(self, radios):
        self.radios = radios