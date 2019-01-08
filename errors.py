
def invalid_response_body(response):
	print(f"ERROR\nThere seems to be no price in the response : {response.json()}")
	return None

def invalid_response_status(response):
	print(f"Error : Status code is {response.status_code}")
	return None

def no_trains_found(response):
	print(f"ERROR\nNo free trains this day : {response.json()}")
	return None