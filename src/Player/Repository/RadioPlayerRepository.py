import json

from src.Player.Core.Model.PlayerInfo import PlayerInfo, StoredPlayerInfo
from src.Player.Core.Model.Radio import Radio


class RadioPlayerRepository:
    def __init__(self, data_folder_path):
        data_folder_path = data_folder_path
        self.radios_file = f'{data_folder_path}/radios.json'
        self.player_file = f'{data_folder_path}/player.json'

    def get_radios(self):
        with open(self.radios_file, "r") as read_file:
            data = json.load(read_file)

        radios = []

        for radio_dictionary in data:
            radio = Radio.from_dictionary(radio_dictionary)
            radios.append(radio)

        return radios

    def get_stored_player_info(self):
        with open(self.player_file, "r") as read_file:
            data = json.load(read_file)

        radio = data['radio']
        volume = data['volume']

        return StoredPlayerInfo(radio, volume)

    def set_player_info(self, player_info):
        with open(self.player_file, "r") as read_file:
            data = json.load(read_file)

        data["volume"] = player_info.volume
        data["radio"] = player_info.radio.id

        with open(self.player_file, "w") as jsonFile:
            json.dump(data, jsonFile)

