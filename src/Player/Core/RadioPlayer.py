import vlc

class RadioPlayer:
    def __init__(self):
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()

    def play(self, url):
        media = self.instance.media_new(url)
        self.player.set_media(media)
        # self.media.parse_with_options(1, 0)

        self.player.play()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            raise Exception('Volume must be between 0 and 100')

        self.player.audio_set_volume(volume)
