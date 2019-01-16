# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainline.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/15 10:37:06 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/15 15:22:26 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import json

import requests
import datetime

import logs
from stations import stations_db

search_url = "https://www.trainline.eu/api/v5_1/search"

def get_search_headers():
	search_headers = {
		"accept": "application/json,text/javascript, */*; q=0.01",
		"content-type": "application/json; charset=UTF-8",
	}
	return search_headers

def get_search_body(params):
	search_body = {
		"departure_date": str(params['date']),
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
	return f"TGVMAX found : \n{result.join(array)}"

def save_to_logs(trains_all, trains_tgvmax):
	logs.debug("Saving the results to disk")
	trains_all_file = open("results/trains_all.json", "w")
	trains_all_file.write(json.dumps(trains_all))
	trains_all_file.close()
	trains_tgvmax_file = open("results/trains_tgvmax.json", "w")
	trains_tgvmax_file.write(json.dumps(trains_tgvmax))
	trains_tgvmax_file.close()

def log_trains(trains):
	for train in trains:
		logs.message(f"> {train['departure_date']} for {str(train['cents'] / 100)}€.")

def search(session, params):
	def launch_search(session, params):
		search_response = session.post(search_url, json=get_search_body(params), headers=get_search_headers())
		search_response.raise_for_status()
		trains_all = search_response.json()['folders']
		trains_tgvmax = [train for train in trains_all if train['cents'] == 0]
		keep_hours = [train['departure_date'] for train in trains_tgvmax]
		log_trains(trains_all)
		save_to_logs(trains_all, trains_tgvmax)
		return format_result(keep_hours)
	result = ""
	while params['start'] < params['end']:
		result += launch_search(session, params)
		params['start'] += 2
	return result
