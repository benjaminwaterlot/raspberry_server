# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainline.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/15 10:37:06 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/22 19:24:00 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import json

import requests
import datetime as dt

import logs
from stations import stations_db

search_url = "https://www.trainline.eu/api/v5_1/search"

def get_search_headers():
	search_headers = {
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
		"accept": "application/json,text/javascript, */*; q=0.01",
		"content-type": "application/json; charset=UTF-8",
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
		logs.message(f"> {train['departure_date']} for {str(train['cents'] / 100)}€.")

def search(params):
	def launch_search(params):
		print("WILL SEND THIS BODY : ")
		print(get_search_body(params))
		search_response = requests.post(search_url, json=get_search_body(params), headers=get_search_headers())
		search_response.raise_for_status()
		trains_all = search_response.json()['folders']
		trains_tgvmax = [train for train in trains_all if train['cents'] == 0]
		trains_buyable = [train for train in trains_tgvmax if train['is_sellable'] == True]
		keep_hours = [train['departure_date'] for train in trains_buyable]
		log_trains(trains_all, trains_tgvmax, trains_buyable)
		save_to_logs(trains_all, trains_tgvmax)
		return format_result(keep_hours)
	result = ""
	while params['time_start'] < params['time_end']:
		result += launch_search(params)
		if params['time_start'].hour >= 21:
			break
		params['time_start'] = params['time_start'].replace(hour=params['time_start'].hour + 3)
	return f"TGVMAX found: \n{result}" if result else "NOTHING!\n"
