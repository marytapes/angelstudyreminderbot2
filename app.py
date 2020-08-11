import random
from flask import Flask, request
from pymessenger.bot import Bot

from time import sleep
from random import randint

import sys

import time
import subprocess

app = Flask(__name__)
ACCESS_TOKEN = 'EAAEEcTiDZAYkBADeLoLBoPFyJCQMwKTbXoccY28DEgChCkjVD58zZBCbQHXxj8eWNZB2dqErZCwZBJDAm3tN6ZAtj6QZAEq989RLsM0ZA3umiRoVnsMaB8koeUyqMcVkmvmJU2bmDbGI5g0cpPNQdPBKadTfpiuNENsIaMJHqpIv8AZDZD'
VERIFY_TOKEN = 'eraumavez'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])

def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message() 
                        while True:
                            send_message(recipient_id, response_sent_text)
                            sleep(14400)    # 14400
                    #if message['message'].get('attachments'):
                     #   response_sent_nontext = get_message()
                      #  send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_message():
    sample_responses = ["Must I remind of you how imporat it is to study?", 
    "MOVE YOUR FUCKING FAT ASS AND GO STUDY!", 
    "STOP PROCRASTINATING AND GO STUDY!",
    "Have you studied today?", 
    "Make me proud, go study.", 
    "Think about all my 7s at HLs... don't you want that?? Then study!", 
    "You need at least a 38 for Pomona. No study, no Pomona."
    "Bitch, whatta ya doin?? Go study!"]
    rand_name = sample_responses[randint(0, len(sample_responses) - 1)]
    return rand_name


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
        app.run()
        
    


