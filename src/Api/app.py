#!flask/bin/python
from flask import Flask, jsonify, make_response
from src.Api.RadioLoader import RadioLoader
from src.Api.RadiosRpcClient import send_message

app = Flask(__name__)
radios = RadioLoader().load()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/radios')
def get_radios():
    print(radios)
    response = make_response(
        jsonify(radios),
        200,
    )
    return response

@app.route('/radios/<int:radio_id>/play', methods=['GET'])
def play_radio(radio_id):

    radio = radios[radio_id]
    send_message('play', radio['url'])

    response = make_response(
        '',
        200,
    )
    return response

@app.route('/radios/<int:radio_id>/stop', methods=['GET'])
def stop_radio(radio_id):
    send_message('stop', '')

    response = make_response(
        '',
        200,
    )
    return response
