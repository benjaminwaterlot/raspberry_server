import json

stations_list = open("stations.json", "r")

stations_db = []

def transcribe(station):
	other_synonyms = []
	if station.find(' ') > 3:
		other_synonyms.append(station.split(' ')[0])
	return {
		'value': station,
		'synonyms': [
			station,
			str.capitalize(station),
			str.lower(station),
			*other_synonyms,
		]
	}

stations_list = json.load(stations_list)
for station in stations_list:
	print(transcribe(station))
	stations_db.append(transcribe(station))

with open("stations_db.json", "w+") as stations_file:
	stations_file.write(json.dumps(stations_db))