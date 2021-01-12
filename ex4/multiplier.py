import pika
import sys
import os
import mysql.connector



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='rand_numbers_queue')

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ex4"
    )


    def callback(ch, method, properties, body):
        numbers_list = body.decode("utf-8").split(',')

        num1, num2 = numbers_list

        sql = f"INSERT INTO Numbers (number1, number2, result) " \
            f"VALUES ({num1}, {num2},{int(num1)*int(num2)})"

        with mydb.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()


    channel.basic_consume(queue='rand_numbers_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' Waiting for numbers ...')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)