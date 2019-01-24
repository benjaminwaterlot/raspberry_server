# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/22 11:56:22 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/24 11:25:30 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
import requests
import json
import trainline.trainline as trainline
import datetime as dt

app = Flask(__name__)

PAGE_TOKEN = "EAALSRXE5200BAJZAZBoM9YEUZCtm429dVIXWe1EIh3U0IKKB1Nb2evh5vtjj2ZA1CRnBkBnZCWynzaaiBupJ8MB7S7Q2fjyDQT3RNMcxIHbiWxHf1Tqx8TrtwihGyOZAWodC5aGRbYcB1QeYlClE5mqFsbCHbVfZAD8f5s0JmszLgZDZD"
VERIFY_TOKEN = "coucou"

@app.route('/bot', methods=['GET'])
def handle_verification():
	if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
		print("Authenticated")
		return request.args.get('hub.challenge', '')
	else:
		print("Wrong token, asshole")
		return "ERROR"


# @app.route('/bot', methods=['POST'])
# def handle_message():
# 	data = request.get_json()
# 	print("MESSAGE RECEIVED : ")
# 	print(data)
# 	if data['object'] == 'page':
# 		for entry in data['entry']:
# 			for messaging_event in entry['messaging']:
# 				if messaging_event.get('message'):
# 					sender_id = messaging_event['sender']['id']
# 		requests.post("https://graph.facebook.com/v2.6/me/messages",
# 			params={"access_token": PAGE_TOKEN},
# 			headers={"Content-Type": "application/json"},
# 			data= json.dumps({
# 				"recipient": {"id": sender_id},
# 				"message": {"text": "JARVIS !"}
# 			}))
# 	return "Okay, bro !"

@app.route('/webhook', methods=['POST'])
def message_from_jarvis():
	body = request.get_json()
	print("THIS IS THE REQUEST RECEIVED :")
	print(body)
	with open('logs/request_from_dialogflow.json', 'w+') as log:
		log.write(json.dumps(body))
	query = body['queryResult']
	if query['intent']['displayName'] == 'search_train':
		query_params = query['parameters']
		params = {
			'date': dt.datetime.fromisoformat(query_params['date']).date(),
			'depart': query_params['from'],
			'arrival': query_params['to'],
			'start': 18,
			'end': 23,
			'time_start': dt.datetime.fromisoformat(query_params['time_period']['startTime']).time(),
			'time_end': dt.datetime.fromisoformat(query_params['time_period']['endTime']).time(),
		}
		# response = {}
		# response['fulfillmentText'] = trainline.search(params)
		response = {
			"fulfillmentMessages": [
			{
				"platform": "FACEBOOK",
				"card": {
					"title": "Title: this is a title",
					"subtitle": "This is an subtitle.  Text can include unicode characters including emoji 📱.",
					"imageUri": "https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png",
					"buttons": [
					{
						"text": "This is a button",
						"postback": "https://assistant.google.com/"
					}
					]
				}
			},
			{
			"platform": "FACEBOOK",
			"card": {
				"title": "Title: this is a title",
				"subtitle": "This is an subtitle.  Text can include unicode characters including emoji 📱.",
				"imageUri": "https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png",
				"buttons": [
				{
					"text": "This is a button",
					"postback": "https://assistant.google.com/"
				}
				]
			}
			}
		]
		}

		# response['fulfillmentMessages'] = [{'messages': [{
		# 		"buttons": [
		# 		{
		# 			"postback": "Card Link URL or text",
		# 			"text": "Card Link Title"
		# 		}
		# 		],
		# 		"imageUrl": "http://urltoimage.com",
		# 		"platform": "facebook",
		# 		"subtitle": "Card Subtitle",
		# 		"title": "Card Title",
		# 		"type": 1
		# 	}]}]
		return json.dumps(response)
	else: exit()
