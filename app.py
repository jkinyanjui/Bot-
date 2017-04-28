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
        if not request.args.get("hub.verify_token") == "KAHIRO":

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

                    # Anticipating Greeting
                if (message_text == "Hello" or "Hi" or "Sasa" or "Niaje" or "Greetings"):
                        if(message_text == "Sasa"):
                            send_message(sender_id, "Sasa rafiki, Unaitwa nani?")
                        elif(message_text == "Niaje"):
                            send_message(sender_id, "Niaje buda, Unaitwa?")
                        elif(message_text == "Hello"):
                            send_message(sender_id, "Hello, What is you're name?")
                        elif(message_text == "Hi"):
                            send_message(sender_id, "Hi. What is your name?")
                        elif():
                            send_message(sender_id, "Still learning greetings but Whats your name?")
                if(message_text == "Kahiro" or "Joy" or "Anita" or "Leez" or "Oliver" or "Weever" or "Paul" or "Wangechi" or "Ibanga" or "Jesica" or "Leo" or "Mandela" or "Chris" or "Daniele" or "Tasha"):
                    if(message_text == "Kahiro"):
                        send_message(sender_id, "Nice to meet you Kahiro. Where did you go to school?")
                    elif(message_text == "Joy"):
                        send_message(sender_id, "Nice to meet you Joy. Where did you go to school?")
                    elif(message_text == "Anita"):
                        send_message(sender_id, "Nice to meet you Anita. Where did you go to school?")
                    elif(message_text == "Leez"):
                        send_message(sender_id, "Nice to meet you Leez. Where did you go to school?")
                    elif(message_text == "Oliver"):
                        send_message(sender_id, "Nice to meet you Oliver. Where did you go to school?")
                    elif(message_text == "Weever"):
                        send_message(sender_id, "Nice to meet you Weever. Where did you go to school?")
                    elif(message_text == "Paul"):
                        send_message(sender_id, "Nice to meet you Paul. Where did you go to school?")
                    elif(message_text == "Wangechi"):
                        send_message(sender_id, "Nice to meet you Wangechi. Where did you go to school?")
                    elif(message_text == "Ibanga"):
                        send_message(sender_id, "Nice to meet you Ibanga. Where did you go to school?")
                    elif(message_text == "Jessica"):
                        send_message(sender_id, "Nice to meet you Jessica. Where did you go to school?")
                    elif(message_text == "Leo"):
                        send_message(sender_id, "Nice to meet you Leo. Where did you go to school?")
                    elif(message_text == "Mandela"):
                        send_message(sender_id, "Nice to meet you Mandela. Where did you go to school?")
                    elif(message_text == "Chris"):
                        send_message(sender_id, "Nice to meet you Chris. Where did you go to school?")
                    elif(message_text == "Daniele"):
                        send_message(sender_id, "Nice to meet you Daniele. Where did you go to school?")
                    elif(message_text == "Tasha"):
                        send_message(sender_id, "Nice to meet you Tasha.Where did you go to school?" )
                    elif():
                        send_message(sender_id, "Nice to meet you. Where did you go to school?")
                if(message_text == "Harvard" or "Oxford" or "Monash" or "Georgia Town" or "Columbia" or "Cambridge" or "University Of California" or "University Of Chicago" or "Cornel" or "University Of Michigan" or "Duke" or "Yale" or "North West" or "Princeton" or "University Of Sydney" ):
                    if(message_text == "Harvard"):
                        send_message(sender_id, "Cool Harvard is a good university. What course are you doing?")
                    elif(message_text == "Oxford"):
                        send_message(sender_id, "Cool Oxford is a good university. What course are you doing?")
                    elif(message_text == "Monash"):
                        send_message(sender_id, "Cool Monash is a good university. What course are you doing?")
                    elif(message_text == "Georgia Tech"):
                        send_message(sender_id, "Cool Georgia Tech is a good university. What course are you doing?")
                    elif(message_text == "Columbia"):
                        send_message(sender_id, "Cool Columbia is a good university. What course are you doing?")
                    elif(message_text == "Cambridge"):
                        send_message(sender_id, "Cool Cambridge is a good university. What course are you doing?")
                    elif(message_text == "University Of California"):
                        send_message(sender_id, "Cool University Of California is a good university. What course are you doing?")
                    elif(message_text == "University Of Chicago"):
                        send_message(sender_id, "Cool University Of Chicago is a good university. What course are you doing?")
                    elif(message_text == "Cornel"):
                        send_message(sender_id, "Cool Cornel is a good university. What course are you doing?")
                    elif(message_text == "University Of Michigan"):
                        send_message(sender_id, "Cool University Of Michigan is a good university. What course are you doing?")
                    elif(message_text == "Duke"):
                        send_message(sender_id, "Cool Duke is a good university. What course are you doing?")
                    elif(message_text == "Yale"):
                        send_message(sender_id, "Cool Yale is a good university. What course are you doing?")
                    elif(message_text == "North West"):
                        send_message(sender_id, "Cool North West is a good university. What course are you doing?")
                    elif(message_text == "Princeton"):
                        send_message(sender_id, "Cool Princeton is a good university. What course are you doing?")
                    elif(message_text == "University Of Sydney"):
                        send_message(sender_id, "Cool University Of Sydney is a good university. What course are you doing?")
                    elif(message_text == "University"):
                        send_message(sender_id, "I don't know where that is but I hope it's a good university. What did you study there?")
                '''if(message_text == {"Course":["Computer Science","IT","Finance","Engineering","Design"]}):
                    send_message(sender_id, "Are you in need of a Job?")
                elif(message_text == "Yes" or "yes"):
                        send_message(sender_id, "Visit our website:www.braveventurelabs.com")
                elif(message_text == "No" or "no"):
                    send_message(sender_id,"What kind of information do you require?")
                else:
                    send_message(sender_id,"We currently do not have job vacancies for you")'''




                #if(message_text == {"courses":["Mass Communication", "Medicine", "Photography", "Computer Science", "Criminology", "Education", "Fashon", "Economics", "Film Making"]})
                #    send_message(sender_id, "Do you have any work experience in this sector?")
                #else():
                #    send_message(sender_id, "Which industry do you want to work in")




            #    else:
            #        send_message(sender_id, "I am still learning")

                    # End of playing with stuff







                    #send_message(sender_id, "roger that!")

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
        "access_token": "EAABuOkHWZCo0BAMYZCtjvKFgbEbwH4Hzu0ptZCAgJ7LrTai6fJbE9POxR29FsthxRLlENvyD0dLSatSbxIOqlAsT4CpTw9jHcQSzDbHOphBSqzAtq8XsqL3yD1KDdaDgs664TmZCvasvR4dpnzhMtRxorLtzPgbd7Rzhc2a2FwZDZD"
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
