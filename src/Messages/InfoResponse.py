from src.Messages.MessageData import MessageData


class InfoResponse(MessageData):
    def __init__(self, info):
        self.info = info
