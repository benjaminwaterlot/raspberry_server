# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainline.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/15 10:37:06 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/24 13:28:01 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import json

import requests
import datetime as dt

import logs
from stations import stations_db
from resources import months

search_url = "https://www.trainline.eu/api/v5_1/search"


def get_search_headers():
	search_headers = {
		'x-ct-timestamp': str(dt.time()),
	}
	return search_headers


def get_search_body(params):
	departure_date = params['date']
	departure_time = params['time_start']
	search_body = {
		"departure_date": str(dt.datetime.combine(departure_date, departure_time)),
		"return_date": None,
		"cuis": {},
		"systems": ["sncf"],
		"exchangeable_part": None,
		"source": None,
		"is_previous_available": False,
		"is_next_available": False,
		"departure_station_id": stations_db[params['depart']],
		"via_station_id": None,
		"arrival_station_id": stations_db[params['arrival']],
		"exchangeable_pnr_id": None,
		"passenger_ids": ["6806966"],
		"card_ids": [
			"690739",
			"977054",
			"1649967"
		]
	}
	return {"search": search_body}


def format_result(hours):
	array = []
	result = ""
	for hour in hours:
		array += hour[11:16]
		array += '\n'
	return result.join(array)


def save_to_logs(trains_all, trains_tgvmax):
	logs.debug("Saving the results to disk")
	with open("results/trains_all.json", "w+") as trains_all_file:
		trains_all_file.write(json.dumps(trains_all))
	with open("results/trains_tgvmax.json", "w+") as trains_tgvmax_file:
		trains_tgvmax_file.write(json.dumps(trains_tgvmax))


def log_trains(trains_all, trains_tgvmax, trains_buyable):
	logs.message(f"{len(trains_all)} TRAINS FOUND.")
	logs.message(f"{len(trains_tgvmax)} TGVMAX FOUND.")
	logs.message(f"{len(trains_buyable)} AVAILABLE TGVMAX FOUND.")
	for train in trains_tgvmax:
		logs.message(f"> {str(train['departure_date'])} for {str(train['cents'] / 100)}€.")


def search(session, params):
	result = []
	future_requests = []
	while params['time_start'] < params['time_end']:
		future_requests.append(session.post(search_url, json=get_search_body(params), headers=get_search_headers()))
		if params['time_start'].hour >= 21:
			break
		params['time_start'] = params['time_start'].replace(hour=params['time_start'].hour + 3)
	
	for request in future_requests:
		response = request.result()
		response.raise_for_status()
		trains_all = response.json()['folders']
		trains_tgvmax = [train for train in trains_all if train['cents'] == 0]
		trains_buyable = [train for train in trains_tgvmax if train['is_sellable'] == True]
		keep_hours = [dt.datetime.fromisoformat(train['departure_date']) for train in trains_buyable]
		log_trains(trains_all, trains_tgvmax, trains_buyable)
		trains = [f"{d.hour}h{d.minute} ({d.day} {months.months[d.month]})" for d in keep_hours]
		for train in trains:
			result.append(train)
	return result
