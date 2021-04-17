from src.Messages.MessageData import MessageData


class PlayResponse(MessageData):
    def __init__(self, error = None):

        if error is None:
            self.success = True
            self.error = ''
        else:
            self.success = False
            self.error = error
