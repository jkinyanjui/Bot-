import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "Bobby":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    # Play with stuff here

                    # Anticipating Greetings
                    if (message_text == "Hello" or "Hi" or  "Greetings"):
                        if(message_text == "Hello"):
                            send_message(sender_id, "Hello,my friend,what is your name?")
                        elif(message_text == "Hi"):
                            send_message(sender_id,"Hi,my friend,what is your name?")
                        elif(message_text == "Greetings"):
                            send_message(sender_id,"Greetings my friend,what is your name?")
                        elif(message_text == "Joy"or"Wangechi"or"Leez"or"Oliver"or"Weever"or"Paul"or"Kahiro"or"Anita"):
                            send_message(sender_id, "Nice to meet you Joy, Where did you go to school?")
                        elif(message_text == "Wangechi"):
                            send_message(sender_id, "Nice to  meet you Wangechi,Where did you go to school?")
                        elif(message_text == "Leez"):
                            send_message(sender_id,"Nice to meet you Leez,Where did you go to school?" )
                        elif(message_text == "Oliver"):
                            send_message(sender_id,"Nice to meet you Oliver,Where did you go  to school?")
                        elif(message_text == "Weever"):
                            send_message(sender_id,"Nice to meet you Weever,Where did you go  to school?")
                        elif(message_text == "Kahiro"):
                            send_message(sender_id,"Nice to meet you Kahiro,Where did you go to school?")
                        elif(message_text == "Paul"):
                            send_message(sender_id,"Nice to meet you Paul,Where did you go  to school?")
                        elif(message_text == "Anita"):
                            send_message(sender_id,"Nice to meet you Oliver,Where did you go  to school?")

                        else:
                            send_message(sender_id,"Hey,What is your name?")
                    else:
                            send_message(sender_id,"I don't know what you mean by that")

                    if (message_text == {"Schools":["Columbia", "Harvard", "Stanford" , "MIT" , "Yale" , "Kimathi"]}):
                        send_message(sender_id, "What course did you take?")
                    else:
                        send_message(sender_id, "Where is that university located?")

                    if(message_text == {"Course":["Computer Science","IT","Finance","Engineering","Design"]}):
                        send_message(sender_id, "Are you in need of a Job?")
                    elif(message_text == "Yes" or "yes"):
                            send_message(sender_id,"Visit our website:Brave Venture Labs")
                    elif(message_text == "No" or "no"):
                        send_message(sender_id,"What kind of information do you require?")
                    else:
                        send_message(sender_id,"We currently do not have job vacancies for you")
                #    if(message_tet == {"Majors":""}):








                    #    '''send_message(sender_id, "What field did you specialise in?")
                    #        elif(message_text == ["Archirecture","Finance","Wed design"]):
                    #                send_message(sender_id,"What is your greatest strength?")
                    #            else(message_text == "Computer Science"):
                    #                send_message(sender_id."Have you been employed before?")'''






                    # End of playing with stuff


                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAALNAlqnhhkBADSRjdhw5TtfAJ24zVC8ZBnOAWsHsZABoTb9FPw2bFPUokeKV5ksDi25YDOcxRhgiXGZAEPx0o37559mUdBb24ZC99HdUQbcJiZAjm7A6tsNcoBVnyZClnGrAPe0MSqpLROwiOPF8cqUcYV9EJL6v704g5R4ffrgZDZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
