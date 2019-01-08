# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stations.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/08 19:39:21 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/08 19:41:26 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

stations_db = {
	'PARIS': 'FRPAR',
	'CHAMBERY': 'FRCMF',
}

def find_station(station):
	station_uppercase = str.upper(station)
	if (station_uppercase in stations_db):
		return stations_db[station_uppercase]
	else:
		return None