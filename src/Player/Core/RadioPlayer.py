import vlc
import os

from src.Player.Core.Model.PlayerInfo import PlayerInfo
from src.Player.Core.Model.Status import *


class RadioPlayer:
    def __init__(self, radio_player_repository):
        self.repository = radio_player_repository
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()

        self.radios = self.repository.get_radios()

        stored_player_info = self.repository.get_stored_player_info()
        stored_radio = next((r for r in self.radios if r.id == stored_player_info.radio_id), None)

        self.info = PlayerInfo(stored_radio, stored_player_info.volume)


    def get_radios(self):
        return self.radios

    def play(self, id):
        radio = next((r for r in self.radios if r.id == id), None)

        self.info.radio = radio
        self.info.status = Status.Loading

        self._save_status()

        media = self.instance.media_new(radio.url)
        self.player.set_media(media)

        self.player.play()

        self.info.status = Status.Playing

        self._save_status()

    def stop(self):
        self.player.stop()
        self.info.status = Status.Stopped

        self._save_status()

    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            raise Exception('Volume must be between 0 and 100')

        self.player.audio_set_volume(volume)
        self.info.volume = self.player.audio_get_volume()

        self._save_status()

    def get_info(self):
        return self.info

    def shutdown(self):
        self.info.status = Status.ShuttingDown
        self._save_status()
        self.stop()
        os.system('shutdown -s')

    def _save_status(self):
        #try:
        self.repository.set_player_info(self.info)
        #except:
        #    print("Error while saving status")

