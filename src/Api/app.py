#!flask/bin/python
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
from src.Api.RadioLoader import RadioLoader
from src.Api.RadiosRpcClient import send_message

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

radios = RadioLoader().load()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/radios')
@cross_origin()
def get_radios():
    print(radios)
    response = make_response(
        jsonify(radios),
        200,
    )
    return response

@app.route('/api/radios/<int:radio_id>/play', methods=['GET'])
@cross_origin()
def play_radio(radio_id):

    radio = radios[radio_id]
    send_message('play', radio['url'])

    response = make_response(
        '{}',
        200,
    )
    return response

@app.route('/api/radios/stop', methods=['GET'])
@cross_origin()
def stop_radio():
    send_message('stop', '')

    response = make_response(
        '',
        200,
    )
    return response

@app.route('/api/radios/volume/<int:volume', methods=['GET'])
@cross_origin()
def change_volume(volume):
    send_message('volume', volume)

    response = make_response(
        '',
        200,
    )
    return response
