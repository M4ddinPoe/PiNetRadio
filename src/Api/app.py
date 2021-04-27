#!flask/bin/python
import logging
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin

from src.Api.RabbitRpcMessageClient import RabbitRpcMessageClient
from src.Logger.Logger import configure_logging
from src.Messages.ChangeVolumeRequest import ChangeVolumeRequest
from src.Messages.PlayRequest import PlayRequest
from src.Messages.RadiosRequest import RadiosRequest
from src.Messages.ShutdownRequest import ShutdownRequest
from src.Messages.StopRequest import StopRequest

configure_logging('piNetRadio-Api')
logging.info('api starting.')

app = Flask(__name__, static_url_path='/static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.info('api started')

#try:
#    radios = RadioLoader().load()
#    logging.debug('loaded radios:')
#    logging.debug(radios)
#except:
#    logging.error('could not load radios.')

rpc_message_client = RabbitRpcMessageClient('localhost', 'radio-player-rpc')

@app.route('/api/radios')
@cross_origin()
def get_radios():
    try:
        logging.debug('/api/radios called')

        request = RadiosRequest()
        response = rpc_message_client.call(request)

        api_response = make_response(
            jsonify(response),
            200,
        )
        return api_response
    except:
        logging.error('error in /radios')
        return make_response('', 500)


@app.route('/api/radios/<int:radio_id>/play', methods=['GET'])
@cross_origin()
def play_radio(radio_id):
    try:
        logging.debug(f'/api/radios/{radio_id}/ play called')

        request = PlayRequest()
        response = rpc_message_client.call(request)

        api_response = make_response(
            jsonify(response),
            200,
        )

        return api_response
    except:
        logging.error(f'/api/radios/{radio_id}/')
        return make_response('', 500)


@app.route('/api/radios/stop', methods=['GET'])
@cross_origin()
def stop_radio():
    try:
        logging.debug('/api/radios/stop called')

        request = StopRequest()
        response = rpc_message_client.call(request)

        api_response = make_response(
            jsonify(response),
            200,
        )

        return api_response
    except:
        logging.error('/api/radios/stop/')
        return make_response('', 500)


@app.route('/api/radios/volume/<int:volume>', methods=['GET'])
@cross_origin()
def change_volume(volume):
    try:
        logging.debug(f'/api/radios/volume/{volume}/ called')

        request = ChangeVolumeRequest(volume)
        response = rpc_message_client.call(request)

        api_response = make_response(
            jsonify(response),
            200,
        )

        return api_response
    except:
        logging.error(f'/api/radios/volume/{volume}/')
        return make_response('', 500)

@app.route('/api/system/shutdown', methods=['GET'])
@cross_origin()
def shutdown():
    try:
        logging.debug(f'/api/system/shutdown/ called')

        request = ShutdownRequest()
        response = rpc_message_client.call(request)

        api_response = make_response(
            jsonify(response),
            200,
        )

        return api_response
    except:
        logging.error(f'/api/system/shutdown/')
        return make_response('', 500)
