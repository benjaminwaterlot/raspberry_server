# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/22 11:56:22 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/24 17:00:10 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
import requests
import json
import trainline.search
import datetime as dt
from requests_futures.sessions import FuturesSession
from utils.text import padded

app = Flask(__name__)

PAGE_TOKEN = "EAALSRXE5200BAJZAZBoM9YEUZCtm429dVIXWe1EIh3U0IKKB1Nb2evh5vtjj2ZA1CRnBkBnZCWynzaaiBupJ8MB7S7Q2fjyDQT3RNMcxIHbiWxHf1Tqx8TrtwihGyOZAWodC5aGRbYcB1QeYlClE5mqFsbCHbVfZAD8f5s0JmszLgZDZD"
VERIFY_TOKEN = "coucou"

session_headers = {
	"accept-language": "fr-FR,fr;q=0.8",
	"authorization": "Token token=\"bn1jmsKj7-EzsyRrx4bt\"",
	"x-ct-client-id": "91f690ff-8005-4203-9145-91567ca4a656",
	"x-ct-version": "8381c2c803382d9064fdd08cf188cf28488da811",
	"x-ct-locale": "fr",
	"x-user-agent": "CaptainTrain/1546957175(web) (Ember 3.4.6)",
	"x-requested-with": "XMLHttpRequest",
	"x-not-a-bot": "i-am-human",
	"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	"referer": "https://www.trainline.eu/search",
	"authority": 'www.trainline.eu',
	"accept": "application/json,text/javascript, */*; q=0.01",
	"content-type": "application/json; charset=UTF-8",
}

@app.before_first_request
def launch_session():
	app.session = FuturesSession()
	app.session.headers.update(session_headers)

@app.route('/bot', methods=['GET'])
def handle_verification():
	if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
		print("Authenticated")
		return request.args.get('hub.challenge', '')
	else:
		print("Wrong token, asshole")
		return "ERROR"


@app.route('/webhook', methods=['POST'])
def message_from_jarvis():
	body = request.get_json()
	print("THIS IS THE REQUEST RECEIVED :")
	print(body)
	query = body['queryResult']
	if 'intent' in query and query['intent']['displayName'] == 'search_train':
		query_params = query['parameters']
		params = {
			'date': dt.datetime.fromisoformat(query_params['date']).date(),
			'depart': query_params['from'],
			'arrival': query_params['to'],
			'time_start': dt.datetime.fromisoformat(query_params['time_period']['startTime']).time(),
			'time_end': dt.datetime.fromisoformat(query_params['time_period']['endTime']).time(),
		}
		response = {}
		trains_found = trainline.search.search(app.session, params)
		if len(trains_found) == 0:
			response['fulfillmentText'] = "Désolé, je n'ai rien trouvé :("
		else:
			replies = [{'content_type': 'text', 'title': train, 'payload': f"coucou cest {train}"} for train in trains_found]
			response['payload'] = {
				'facebook': {
					'text': f"*{len(trains_found)} TGVmax dispo*\n"
							f"_({params['depart']} > {params['arrival']}, le {padded(params['date'].day)} "
							f"entre {padded(params['time_start'].hour)}h{padded(params['time_start'].minute)}"
							f" et {padded(params['time_end'].hour)}h{padded(params['time_end'].minute)})_",
					"quick_replies": replies
				}
			}
			# 'facebook': {
			# 	"text": "Here is a quick reply!",
			# 	"quick_replies":[
			# 	{
			# 		"content_type":"text",
			# 		"title":"Search",
			# 		"payload":"<POSTBACK_PAYLOAD>",
			# 		"image_url":"http://example.com/img/red.png"
			# 	},
			# 	{
			# 		"content_type":"location"
			# 	}
			# 	]
			# }
			# response['fulfillmentMessages'] = [{
			# 	"platform": "FACEBOOK",
			# 	"quick_replies": {
			# 		'title': f"*{len(trains_found)} TGVmax dispo*\n"
			# 				 f"_({params['depart']} > {params['arrival']}, le {padded(params['date'].day)} "
			# 				 f"entre {padded(params['time_start'].hour)}h{padded(params['time_start'].minute)}"
			# 				 f" et {padded(params['time_end'].hour)}h{padded(params['time_end'].minute)})_",
			# 			"quickReplies": trains_found
			# 	}}]
		return json.dumps(response)
	else: exit()
