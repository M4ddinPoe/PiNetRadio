from src.Player.Core.RadioPlayer import RadioPlayer
from src.Player.Core.RadioLoader import RadioLoader


class RadioPlayerConsole:
    def __init__(self, data_path):
        radio_loader = RadioLoader(data_path)
        self.radio_player = RadioPlayer(radio_loader)

        self.commands = {'show': self.show_radios,
                         'play': self.play,
                         'stop': self.stop,
                         'volume': self.set_volume,
                         'status': self.show_status}

    def run(self):

        is_running = True

        while is_running:
            command, parameter = self._read_input()

            if command == 'q':
                is_running = False
            else:
                self.commands[command](parameter)

    def show_radios(self, parameter):
        radios = self.radio_player.get_radios()

        for radio in radios:
            print(f'{radio.id}: {radio.title}')

    def play(self, id):
        self.radio_player.play(id)

    def stop(self, parameter):
        self.radio_player.stop()

    def set_volume(self, volume):
        self.radio_player.set_volume(volume)

    def show_status(self, parameter):
        status = self.radio_player.get_status()
        print(status.to_text())

    @staticmethod
    def _read_input():
        user_input = input()

        parts = user_input.split(' ')

        if len(parts) == 1:
            return parts[0], None

        if len(parts) == 2:
            return parts[0], int(parts[1])


app = RadioPlayerConsole('../Data/radios.json')
app.run()
