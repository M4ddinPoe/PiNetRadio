import pika

def send_message(command, url):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='radio-player', exchange_type='fanout')

    message = '{ "command":"%s", "url": "%s" }' %(command, url)
    channel.basic_publish(exchange='radio-player', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()