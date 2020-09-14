import json

class RadioLoader:
    def __init__(self):
        self.filePath = 'radios.json'

    def load(self):
        with open(self.filePath, "r") as read_file:
            radios = json.load(read_file)

        return radios
