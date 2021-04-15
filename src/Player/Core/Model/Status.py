

class Status:
    def to_text(self):
        return "Unknown"


class StoppedStatus(Status):
    def to_text(self):
        return "Stopped"


class LoadingStatus(Status):
    def __init__(self, radio):
        self.radio = radio

    def to_text(self):
        return f"Loading: {self.radio.title}"


class PlayingStatus(Status):
    def __init__(self, radio, volume):
        self.radio = radio
        self.volume = volume

    def to_text(self):
        return f"Playing: {self.radio.title} at volume '{self.volume}'"


class ShuttingDownStatus(Status):
    def to_text(self):
        return "Shutting down"