import vlc
import os

from src.Player.Core.Model.Radio import Radio
from src.Player.Core.Model.Status import *


class RadioPlayer:
    def __init__(self, radio_loader):
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()
        self.status = StoppedStatus()
        self.radios = []
        radios_dictionary = radio_loader.load()

        for radio_dictionary in radios_dictionary:
            radio = Radio.from_dictionary(radio_dictionary)
            self.radios.append(radio)

    def get_radios(self):
        return self.radios

    def get_status(self):
        return self.status

    def play(self, id):
        radio = next((r for r in self.radios if r.id == id), None)
        self.status = LoadingStatus(radio)

        volume = self.player.audio_get_volume()

        media = self.instance.media_new(radio.url)
        self.player.set_media(media)
        # self.media.parse_with_options(1, 0)

        self.player.play()

        self.status = PlayingStatus(radio, volume)

    def stop(self):
        self.player.stop()
        self.status = StoppedStatus()

    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            raise Exception('Volume must be between 0 and 100')

        self.status.volume = self.player.audio_get_volume()
        self.player.audio_set_volume(volume)

    def get_status(self):
        return self.status

    def get_info(self):
        is_playing = self.player.is_playing()

        if is_playing:
            info = self.media.parse_with_options(1, 0)

        return { is_playing, info }

    def shutdown(self):
        self.status = ShuttingDownStatus()
        self.stop()
        os.system('shutdown -s')
