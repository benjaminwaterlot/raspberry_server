// REQUEST
fetch("https://www.trainline.fr/api/v5_1/book",
{
	"credentials": "include",
	"headers":
	{
		"accept": "application/json, text/javascript, */*; q=0.01",
		"accept-language": "fr-FR,fr;q=0.8",
		"authorization": "Token token=\"bK_zn2Pgy-GmuzCQixsH\"",
		"content-type": "application/json; charset=UTF-8",
		"x-ct-client-id": "88a79bfc-6b02-4d80-8cb8-8777321a8b2a",
		"x-ct-locale": "fr",
		"x-ct-timestamp": "1547739250",
		"x-ct-version": "a93f675d7029d79cb5be740a8d285b2600777251",
		"x-not-a-bot": "i-am-human",
		"x-requested-with": "XMLHttpRequest",
		"x-user-agent": "CaptainTrain/1547739250(web) (Ember 3.4.6)"
	},
	"referrer": "https://www.trainline.fr/search/chambery-challes-les-eaux/paris/2019-01-28-18:00",
	"referrerPolicy": "no-referrer-when-downgrade",
	"body":
	{
		"book":
		{
			"search_id": "376892425",
			"outward_folder_id": "140f5ca41cc511e99ae72b20f54659a3",
			"options":
			{
				"140f57681cc511e98b3bebd92d79b3ad":
				{
					"comfort_class": "pao.default",
					"seat": "no_preference"
				}
			}
		}
	},
	"method": "POST",
	"mode": "cors"
});

// RESPONSE BODY
var response_body = {
	"pnrs": [
		{
			"id": "32449277",
			"after_sale_url": "",
			"alterable_passengers_parts": [],
			"booking_status": "booked",
			"cents": 0,
			"currency": "EUR",
			"exchangeable_parts": [],
			"formatted_instructions": {
				"primary": "E-billet nominatif stocké dans la carte Voyageur."
			},
			"is_printed": false,
			"local_amount": {
				"subunit": 0,
				"subunit_to_unit": 100
			},
			"local_currency": "EUR",
			"messages": [],
			"refundable_parts": [],
			"revision": "47956375",
			"sort_date": "2019-01-29T06:25:00+01:00",
			"system": "pao_sncf",
			"public_token": "mfumxaoaicfocb",
			"terms_of_transportation": [
				"sncf"
			],
			"invoice_available": false,
			"is_paid": false,
			"is_quarantined": false,
			"is_emission_in_progress": false,
			"needs_identification": false,
			"needs_refresh": false,
			"is_classic": false,
			"is_eticket": true,
			"is_mticket": true,
			"is_ticketless": false,
			"is_emitted": false,
			"reservation_name": "WATERLOT",
			"hide_ticket_time_limit": false,
			"ticket_time_limit": "2019-01-22T06:20:00+01:00",
			"safe_ticket_time_limit": "2019-01-22T06:20:00+01:00",
			"is_selected": true,
			"after_sales_log_ids": [],
			"booker_id": "570318",
			"folder_ids": [
				"56304142"
			],
			"group_id": "vevqaoslmsngnf",
			"user_id": "570318",
			"order_id": null,
			"travel_document_ids": [],
			"mgmt_info_captured_values": []
		}
	],
	"folders": [
		{
			"id": "56304142",
			"arrival_date": "2019-01-29T09:15:00+01:00",
			"cents": 0,
			"currency": "EUR",
			"departure_date": "2019-01-29T06:25:00+01:00",
			"digest": "3b358f8bb4a39aa37426643509a4f34572012569",
			"direction": "outward",
			"local_amount": {
				"subunit": 0,
				"subunit_to_unit": 100
			},
			"local_currency": "EUR",
			"system": "pao_sncf",
			"arrival_station_id": "4924",
			"departure_station_id": "1339",
			"pnr_id": "32449277",
			"trip_ids": [
				"76199868"
			]
		}
	],
	"trips": [
		{
			"id": "76199868",
			"arrival_date": "2019-01-29T09:15:00+01:00",
			"cents": 0,
			"currency": "EUR",
			"departure_date": "2019-01-29T06:25:00+01:00",
			"local_amount": {
				"subunit": 0,
				"subunit_to_unit": 100
			},
			"local_currency": "EUR",
			"arrival_station_id": "4924",
			"departure_station_id": "1339",
			"folder_id": "56304142",
			"passenger_id": "3d039552-ffe4-4ece-9384-c91f242b8b39",
			"segment_ids": [
				"94572787"
			]
		}
	],
	"segments": [
		{
			"id": "94572787",
			"arrival_date": "2019-01-29T09:15:00+01:00",
			"brand": "tgvmax",
			"co2_emission": 1800,
			"car": "8",
			"carrier": "sncf",
			"departure_date": "2019-01-29T06:25:00+01:00",
			"digest": "29b5846d68a33f65582d2fd167ac6e16c1cfd329",
			"formatted_seating": "bas, côte à côte, couloir",
			"locale_keys_for_formatted_seating": [
				{
					"seating.lower_deck": {}
				},
				{
					"seating.twin": {}
				},
				{
					"seating.aisle": {
						"count": 1,
						"pluralization_key": "one"
					}
				}
			],
			"seat": "24",
			"seat_type": "seat",
			"train_number": "6960",
			"travel_class": "economy",
			"transportation_mean": "train",
			"arrival_station_id": "4924",
			"condition_id": "13581",
			"cui_id": null,
			"departure_station_id": "1339",
			"trip_id": "76199868",
			"is_refundable": true,
			"train_name": "TGV",
			"reservation": "reserved"
		}
	],
	"conditions": [
		{
			"id": "13581",
			"name": "TGVmax",
			"digest": "233576189",
			"short_description": "Tout billet TGVMAX doit être reconfirmé 2 jours avant le départ. Annulation automatique des billets non confirmés la veille à 17h. Billet non échangeable. Pièce d'identité à présenter à bord du train. Aucune photocopie ou scan ne sera accepté(e).",
			"long_description": [
				{
					"title": "Conditions",
					"body": "Tout billet TGVMAX doit être reconfirmé 2 jours avant le départ. Annulation automatique des billets non confirmés la veille à 17h. Billet non échangeable. Pièce d'identité à présenter à bord du train. Aucune photocopie ou scan ne sera accepté(e)."
				}
			]
		}
	],
	"cuis": [],
	"passengers": [
		{
			"id": "3d039552-ffe4-4ece-9384-c91f242b8b39",
			"first_name": "Benjamin",
			"gender": "male",
			"last_name": "Waterlot",
			"kind": "human",
			"is_animal": false,
			"is_owned": true,
			"original_id": "6806966",
			"birthdate": "1993-12-06T00:00:00+00:00"
		}
	],
	"stations": [
		{
			"id": "1339",
			"is_sellable": true,
			"name": "Chambéry Challes-les-Eaux",
			"slug": "chambery-challes-les-eaux",
			"country": "FR",
			"score": 0.0131877133735082,
			"info": null,
			"parent_name": "Chambéry",
			"parent_slug": "chambery",
			"latitude": 45.571302,
			"longitude": 5.919547
		},
		{
			"id": "4924",
			"is_sellable": true,
			"name": "Paris Gare de Lyon",
			"slug": "paris-gare-de-lyon",
			"country": "FR",
			"score": 0.0917608563881259,
			"info": null,
			"parent_name": "Paris",
			"parent_slug": "paris",
			"latitude": 48.844888,
			"longitude": 2.37352
		}
	],
	"proofs": [],
	"participants": [
		{
			"id": "570318",
			"first_name": "Benjamin",
			"last_name": "Waterlot",
			"gender": "male",
			"user_id": "570318"
		}
	],
	"after_sales_logs": [],
	"travel_documents": [],
	"book": {
		"id": "376892425",
		"pnr_ids": [
			"32449277"
		],
		"order_id": null
	}
}