from src.Messages.MessageData import MessageData


class ChangeVolumeRequest(MessageData):
    def __init__(self, volume):
        self.volume = volume