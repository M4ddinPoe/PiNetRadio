from src.Player.Core.RadioPlayer import RadioPlayer
from src.Logger.Logger import configure_logging
from src.Player.MessageHandler.PlayerMessageHandler import PlayerMessageHandler
from src.Player.MessageHandler.RabbitRpcMessageServer import RabbitRpcMessageServer
from src.Player.Repository.RadioPlayerRepository import RadioPlayerRepository

configure_logging('radio_player')

rpc_message_server = RabbitRpcMessageServer('localhost', 'radio-player-rpc')
repository = RadioPlayerRepository('src/Player/Data')
player = RadioPlayer(repository)

player_message_handler = PlayerMessageHandler(rpc_message_server, player)


