from src.Messages.MessageData import MessageData


class PlayResponse(MessageData):
    def __init__(self):
        self.success = True
        self.error = ''

    def __init__(self, success, error):
        self.success = success
        self.error = error

