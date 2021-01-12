import pika
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rand_numbers_queue')

random_numbers_list = []

for i in range(100):
    random_numbers = f'{random.randint(1, 100)}, {random.randint(1, 100)}'
    random_numbers_list.append(random_numbers+'\n')

    channel.basic_publish(exchange='', routing_key='rand_numbers_queue',
                          body=random_numbers)

connection.close()

with open('generated_test_file.txt', 'w') as f:
    f.writelines(random_numbers_list)
