# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/08 19:11:00 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/08 20:00:14 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask
import requests
import stations
import logs
import endpoints

app = Flask(__name__)

def find_trains(departure, arrival, date):
	# url = f"{endpoints['availability']}/{departure}/{arrival}/{date}/{date}/{other_options}"
	url = endpoints.availability(departure, arrival, date)
	response = requests.get(url)
	return (trains_from_response(response))

def trains_from_response(response):
	if (response.status_code != 200):
		return logs.invalid_response_status(response)
	trains = response.json()[0]
	if (trains is None or 'price' not in trains):
		return logs.invalid_response_body(response)
	if (trains['price'] != 0):
		return logs.no_trains_found(response)
	return (trains)

def get_hours_from_trains(trains):
	text = ""
	for hour in trains['hours']:
		text += "\n==============================\n"
		text += hour
	return text

@app.route('/find/<depart>/<destination>/<date>')
def get_availability(depart, destination, date):
	if (not all([depart, destination, date])):
		return logs.bad_arguments(depart, destination, date)
	depart_station = stations.find_station(depart)
	destination_station = stations.find_station(destination)
	if (not all([depart_station, destination_station])):
		logs.bad_station(depart, destination)
		return "BAD STATIONS!"
	trains = find_trains(depart_station, destination_station, date)
	if (trains is None):
		return "NOTHING FOUND!"
	logs.trains_found(trains)
	return f"For the {depart_station} - {destination_station} : {get_hours_from_trains(trains)}"
