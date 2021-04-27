# PiNetRadio
Internet radio player for Raspberry Pi or other single board computer

# About

The piNetRadio is able to play different Internet Radios based on a configuration file.

The PiNetRadio consists of three parts.

1. The Player User Interface
2. A Rest Api
3. The player

The user interface connects with the api over http and returns the configuration can start a radio. The api then communicates with the player over RabbitMq.

# Setup

1. Clone the repository

2. Install python packages

```
pip install flask
pip install flask-cors
pip install pika
pip install python-vlc 
```

3. Install RabbitMQ  
https://www.rabbitmq.com/download.html

4. Make sure VLC Player is installed on your system

# Start-up

## Player
```
python runPlayer.py
```

## API
```
cd src/Api
flask run
```

## Frontend

```
cd src/WebFrontend
npm install
npm run
```