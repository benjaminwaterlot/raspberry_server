# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logs.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/08 19:11:04 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/08 19:58:52 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# COLORS FOR PRINTING ERRORS
class _colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m' 

# CALLERS
def _print_error(message):
	print(_colors.FAIL + _colors.BOLD + "ERROR\n" + message + _colors.END)
	return None

def _print_warning(message):
	print(_colors.WARNING + _colors.BOLD + "WARNING\n" + message + _colors.END)
	return None

def _print_log(message):
	print(_colors.OKGREEN + _colors.BOLD + "EVENT\n" + message + _colors.END)
	return None

# ERRORS
def invalid_response_body(response):
	return _print_error(f"There seems to be no price in the response: {response.json()}")

def invalid_response_status(response):
	return _print_error(f"Status code is {response.status_code}")

def bad_arguments(depart, destination, date):
	return _print_error(f"Bad arguments. Depart: {depart}, destination: {destination}, date: {date}")

def bad_station(station1, station2):
	return _print_error(f"The stations are not recognized: {station1}, {station2}")

# WARNINGS
def no_trains_found(response):
	return _print_warning(f"No free trains this day: {response.json()}")

# LOGS
def trains_found(trains):
	return _print_log(f"{len(trains['hours'])} trains found : {trains['hours']}")