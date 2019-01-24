# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bwaterlo <bwaterlo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/24 15:53:04 by bwaterlo          #+#    #+#              #
#    Updated: 2019/01/24 16:36:41 by bwaterlo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

book_url = "https://www.trainline.fr/api/v5_1/book"


def get_book_body():
	body = {
		"search_id": None, # example : "376892425"
		"outward_folder_id": None, # "140f5ca41cc511e99ae72b20f54659a3"
		"options":
		{
			"140f57681cc511e98b3bebd92d79b3ad":
			{
				"comfort_class": "pao.default",
				"seat": "no_preference"
			}
		}
	}
	return {'book': body}

def book(session, search_id, folder_id, train_id):
	pass