from flask import Flask
import requests

app = Flask(__name__)

endpoint = 'https://www.oui.sncf/apim/calendar/train/v4'
stations = {
	'departure': 'FRPAR',
	'arrival': 'FRCMF'
}
dates = {
	'start': '2019-01-22',
	'end': '2019-01-23'
}
other_options = "12-HAPPY_CARD/2/fr?additionalFields=hours&currency=EUR"
# test = 'https://www.oui.sncf/apim/calendar/train/v4/FRPAR/FRCMF/2019-01-17/2019-01-23/12-HAPPY_CARD/2/fr?additionalFields=hours&currency=EUR'
# call = requests.get(url)

def request(departure, arrival, date):
	return requests.get(f"{endpoint}/{departure}/{arrival}/{date}/{date}/{other_options}").json()[0]['date']

# @app.route('/')
# def index():
# 	return f'Hello you ! The url is `{url}` and the status code is {call.status_code}. The result is {call.json()[0]["date"]}'

@app.route('/example')
def example():
	return request('FRPAR', 'FRCMF', '2019-01-23')

