from src.Messages.MessageData import MessageData


class PlayRequest(MessageData):
    def __init__(self, id):
        self.id = id
