from src.Messages.MessageData import MessageData


class ShutdownResponse(MessageData):
    def __init__(self, success=True, error=''):
        self.success = success
        self.error = error