import pika

def send_message(command, data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='radio-player', exchange_type='fanout')

    message = '{ "command":"%s", "data": "%s" }' %(command, str(data))
    channel.basic_publish(exchange='radio-player', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()