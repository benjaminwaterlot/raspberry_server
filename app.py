# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/08 19:11:00 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/21 17:16:57 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime as dt
import re

from flask import Flask, request
import requests

from logs import debug
import logs
import trainline.trainline as trainline
from stations import stations_db
import parser

app = Flask(__name__)

@app.before_first_request
def startup():
	logs.message("SERVER LAUNCHED !")

def get_session_headers(session):
	session_headers = {
		'x-ct-timestamp': str(dt.time()),
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
	}
	session.headers.update(session_headers)
	return (session)

def refine_query(depart, arrival, date, start, end):
	query = {}
	query['depart'] = depart if (depart and depart in stations_db) else logs.bad_arguments(depart, arrival, date)
	query['arrival'] = arrival if (arrival and arrival in stations_db) else logs.bad_arguments(depart, arrival, date)

	if (dt.date.fromisoformat(date)):
		query['date'] = dt.date.fromisoformat(date)
	else:
		raise ValueError('A very specific bad thing happened.')

	for time in [start, end]:
		if (not int(time) or not (0 <= int(time) <= 24)):
			raise ValueError('Error in the start or end values, should be ints.')
	query['start'] = int(start)
	query['end'] = int(end)
	if (query['start'] > query['end']):
		raise ValueError('You entered a bigger hour end than hour start, moron.')
	return query

@app.route('/')
def home():
	return "Bonjour !"

@app.route('/bot')
def handle_bot_message():
	session = requests.Session()
	session = get_session_headers(session)
	request_body = request.get_json()
	if not request_body:
		return "ERROR IN PARSER, BRO"
	query = parser.parser(request.get_json())
	if query['type'] == 'search':
		return trainline.search(session, query)
	return "Error in parser"

@app.route('/<depart>/<arrival>/<date>/<start>/<end>')
def test(depart = None, arrival = None, date = None, start = '08', end = '22'):
	params = refine_query(depart, arrival, date, start, end)
	session = requests.Session()
	session = get_session_headers(session)
	return trainline.search(session, params)
