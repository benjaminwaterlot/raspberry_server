# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/22 11:56:22 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/22 16:55:36 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
import requests
import json
import trainline.trainline as trainline

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


@app.route('/bot', methods=['POST'])
def handle_message():
	data = request.get_json()
	print("MESSAGE RECEIVED : ")
	print(data)
	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				if messaging_event.get('message'):
					sender_id = messaging_event['sender']['id']
		requests.post("https://graph.facebook.com/v2.6/me/messages",
			params={"access_token": PAGE_TOKEN},
			headers={"Content-Type": "application/json"},
			data= json.dumps({
				"recipient": {"id": sender_id},
				"message": {"text": "JARVIS !"}
			}))
	return "Okay, bro !"

@app.route('/webhook', methods=['POST'])
def message_from_jarvis():
	body = request.get_json()
	print("THIS IS THE REQUEST RECEIVED :")
	print(body)
	query = body['queryResult']
	params = {}
	if query['intent']['displayName'] == 'search_train':
		params['']

	# TODO : TRANSFERER LES PARAMS DEPUIS LA QUERY VERS PARAMS POUR FAIRE LA REQUETE TRAINLINE
	response = {}
	response['fulfillmentText'] = trainline.search(params)
	return json.dumps(response)
