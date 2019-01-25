# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trains.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: benjamin <benjamin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/25 17:26:03 by benjamin          #+#    #+#              #
#    Updated: 2019/01/25 17:27:47 by benjamin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime as dt

from utils.text import padded
from resources.months import months


def format_trainlist(trains_buyable):
    keep_hours = [
        dt.datetime.fromisoformat(train["departure_date"]) for train in trains_buyable
    ]
    trains = [
        f"{padded(d.hour)}h{padded(d.minute)} ({padded(d.day)} {months[d.month]})"
        for d in keep_hours
    ]
    return trains

