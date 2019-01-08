# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    endpoints.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/08 19:41:43 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/08 19:44:19 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

endpoints = {
	'availability': 'https://www.oui.sncf/apim/calendar/train/v4',
}

other_options = "12-HAPPY_CARD/2/fr?additionalFields=hours"

def availability(depart_station, destination_station, date):
	return f'https://www.oui.sncf/apim/calendar/train/v4/{depart_station}/{destination_station}/{date}/{date}/{other_options}'

