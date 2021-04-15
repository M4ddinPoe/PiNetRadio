from src.Player.Core.Model.Status import Status


class PlayerInfo:

    def __init__(self, radio, volume):
        self.volume = volume
        self.radio = radio
        self.status = Status.Stopped


class StoredPlayerInfo:

    def __init__(self, radio_id, volume):
        self.volume = volume
        self.radio_id = radio_id

