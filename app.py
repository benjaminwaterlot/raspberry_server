from flask import Flask
import requests

app = Flask(__name__)

# url_model = '${endpoint}/${origin}/${destination}/${date}/${options.discount}/${options.class}/${options.language}?onlyDirectTrains=${options.direct}&currency=${options.currency}'
# origin = 'FRPAR'
# destination = 'DEFRA'
# date = '2018-01-21'
# options = {
# 	'discount': '26-NO_CARD',
# 	'currency': 'EUR',
# 	'level': 2,
# 	'lang': 'fr',
# 	'direct': 'false'
# }

endpoint = 'https://www.oui.sncf/apim/calendar/train/v4'
stations = {
	'departure': 'FRPAR',
	'arrival': 'FRCMF'
}
dates = {
	'start': '2019-01-22',
	'end': '2019-01-23'
}

# url = F"{endpoint}/{origin}/{destination}/{date}/{options['discount']}/{options['level']}/{options['lang']}?onlyDirectTrains={options['direct']}&currency={options['currency']}"
# url = F"{endpoint}/{origin}/{destination}/{date}/{options['discount']}/{options['level']}/{options['lang']}"
test = 'https://www.oui.sncf/apim/calendar/train/v4/FRPAR/FRCMF/2019-01-17/2019-01-23/12-HAPPY_CARD/2/fr?additionalFields=hours&currency=EUR'
url = f"{endpoint}/{stations['departure']}/{stations['arrival']}/{dates['start']}/{dates['end']}/12-HAPPY_CARD/2/fr?additionalFields=hours&currency=EUR"
call = requests.get(url)

@app.route('/')
def Hello():
	return f'Hello you ! The url is `{url}` and the status code is {call.status_code}. The result is {call.json()[0]["date"]}'
