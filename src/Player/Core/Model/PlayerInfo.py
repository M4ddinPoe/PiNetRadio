from src.Player.Core.Model.Status import Status


class PlayerInfo:

    def __init__(self, radio, volume, status):
        self.volume = volume
        self.radio = radio
        self.status = status
