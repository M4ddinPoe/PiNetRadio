from src.Player.MessageHandler.PlayHandler import PlayHandler
from src.Logger.Logger import configure_logging

configure_logging('radio_player')

radioServer = PlayHandler()
radioServer.start()


