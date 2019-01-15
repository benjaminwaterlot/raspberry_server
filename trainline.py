import requests

search_url = "https://www.trainline.eu/api/v5_1/search"

search_headers = {
	"accept": "application/json,text/javascript, */*; q=0.01",
	"accept-language": "fr-FR,fr;q=0.8",
	"authorization": "Token token=\"bn1jmsKj7-EzsyRrx4bt\"",
	"content-type": "application/json; charset=UTF-8",
	"x-ct-client-id": "91f690ff-8005-4203-9145-91567ca4a656",
	"x-ct-locale": "fr",
	"x-ct-timestamp": "1546957175",
	"x-ct-version": "8381c2c803382d9064fdd08cf188cf28488da811",
	"x-not-a-bot": "i-am-human",
	"x-requested-with": "XMLHttpRequest",
	"x-user-agent": "CaptainTrain/1546957175(web) (Ember 3.4.6)",
	"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	"referer": "https://www.trainline.eu/search",
	"authority": 'www.trainline.eu',
	'x-ct-timestamp': "1546957175",
}

search_body = {
	"search":
	{
		"departure_date": "2019-01-29T10:00:00UTC",
		"return_date": None,
		"cuis": {},
		"systems": ["sncf"],
		"exchangeable_part": None,
		"source": None,
		"is_previous_available": False,
		"is_next_available": False,
		"departure_station_id": "4916",
		"via_station_id": None,
		"arrival_station_id": "1339",
		"exchangeable_pnr_id": None,
		"passenger_ids": ["6806966"],
		"card_ids": [
			"690739",
			"977054",
			"1649967"
		]
	 }
}

def get_search(departure, arrival, date):
	return {'body': search_body, 'headers': search_headers}


def search_to_text(hours):
	array = []
	result = ""
	for hour in hours:
		array += hour[11:16]
		array += '\n'
	return result.join(array)

def search():
	infos = get_search('PARIS', 'CHAMBERY', '2019-01-29')
	search_request = requests.post(search_url, json=infos['body'], headers=infos['headers'])
	search_request.raise_for_status()
	all_trains = search_request.json()['folders']
	only_tgvmax = [train for train in all_trains if train['cents'] == 0]
	keep_hours = [train['departure_date'] for train in only_tgvmax]
	to_text = search_to_text(keep_hours)
	return to_text
