from kafka import KafkaConsumer
import sys
import sys
sys.path.append('../')
from queue_site.log import setup_custom_logger
import smtplib, ssl
from argparse import ArgumentParser
import time
import json


class Mail:
    order_info_message = "здравствуйте долбоеб вот ваш номер {id}"
    def __init__(self,topic:str,partition:int,bootstrap_servers:list):
        self.logger = setup_custom_logger(f'email_sender {partition}','../app.log')
        self.topic = topic
        self.partition = partition
        self.bootstrap_servers = bootstrap_servers
        self.consumer = KafkaConsumer(topic
        ,bootstrap_servers = bootstrap_servers,
                                      auto_offset_reset = 'earliest'
                                       )

        # self.server = smtplib.SMTP('smtp.yandex.ru', 465)
        #
        # self.server.starttls()
        # self.server.ehlo()
        # self.email_sender = email_sender
        # self.email_pass = email_pass


    def start_consuming(self):
        # try:
        #
        #     self.server.login(self.email_sender, self.email_pass)
        #     self.server.ehlo()
        # except Exception as e:
        #     logger.error(e)
        for message in self.consumer:
            print(args.partition)

            if message.partition == self.partition:
                msg = json.loads(message.value)
                email = msg['email']
                type = msg['type']
                id = msg['order_id']

                self.logger.info(f"successfully sent order info to {email}")

        # self.server.sendmail(self.email_sender, email, self.order_info_message % id)


parser = ArgumentParser()
parser.add_argument("-prt", "--partition", dest="partition",
                    help="write report to FILE", metavar="FILE")


args = parser.parse_args()
mail = Mail(topic = "email_sender",partition = int(args.partition),
            bootstrap_servers = ['localhost:9092']
          )

mail.start_consuming()