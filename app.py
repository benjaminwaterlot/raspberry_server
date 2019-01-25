# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: benjamin <benjamin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/25 15:37:52 by benjamin          #+#    #+#              #
#    Updated: 2019/01/25 18:07:06 by benjamin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime as dt
import json

from requests_futures.sessions import FuturesSession
from flask import Flask, request
import requests
import trainline.search

from utils.text import padded
from utils.trains import format_trainlist
from resources.trainline_headers import session_headers
import creds.creds as creds

app = Flask(__name__)


# contexts = []


@app.before_first_request
def open_session():
    app.session = FuturesSession()
    app.session.headers.update(session_headers)


@app.route("/bot", methods=["GET"])
def handle_verification():
    if request.args.get("hub.verify_token", "") == creds.VERIFY_TOKEN:
        print("Authenticated")
        return request.args.get("hub.challenge", "")
    else:
        print("Wrong token, asshole")
        return "ERROR"


@app.route("/webhook", methods=["POST"])
def message_from_jarvis():
    body = request.get_json()
    print("THIS IS THE REQUEST RECEIVED :")
    print(body)
    query = body["queryResult"]
    # sender = body['originalDetectIntentRequest']['payload']['data']['sender']['id']

    if "intent" in query and query["intent"]["displayName"] == "search_train":
        # contexts = []
        # contexts.append({'sender': sender})
        params = query["parameters"]
        params = {
            "date": dt.datetime.fromisoformat(params["date"]).date(),
            "depart": params["from"],
            "arrival": params["to"],
            "time_start": dt.datetime.fromisoformat(
                params["time_period"]["startTime"]
            ).time(),
            "time_end": dt.datetime.fromisoformat(
                params["time_period"]["endTime"]
            ).time(),
        }
        response = {}
        trains_found = trainline.search.search(app.session, params)
        formatted_trains = format_trainlist(trains_found)
        if len(trains_found) == 0:
            response["fulfillmentText"] = "Désolé, je n'ai rien trouvé :("
        else:
            replies = [
                {
                    "content_type": "text",
                    "title": formatted_trains[index],
                    "payload": F"BOOK TRAIN {index}",
                }
                for index, train in enumerate(trains_found)
            ]
            response["payload"] = {
                "facebook": {
                    "text": f"*{len(trains_found)} TGVmax dispo*\n"
                    f"_({params['depart']} > {params['arrival']}, le {padded(params['date'].day)} "
                    f"entre {padded(params['time_start'].hour)}h{padded(params['time_start'].minute)}"
                    f" et {padded(params['time_end'].hour)}h{padded(params['time_end'].minute)})_",
                    "quick_replies": replies,
                }
            }
        print("SENDING THIS PAYLOAD:")
        print(response)
        return json.dumps(response)
    else:
        exit()
