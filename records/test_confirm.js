var request_url_confirm = "https://www.trainline.fr/api/v5_1/payments/17527204/confirm" // ATTENTION LE CODE

// REQUEST
fetch("https://www.trainline.fr/api/v5_1/payments/17527204/confirm",
{
	"credentials": "include",
	"headers":
	{
		"accept": "application/json, text/javascript, */*; q=0.01",
		"accept-language": "fr-FR,fr;q=0.8",
		"authorization": "Token token=\"bK_zn2Pgy-GmuzCQixsH\"",
		"content-type": "application/json; charset=UTF-8",
		"x-ct-client-id": "88a79bfc-6b02-4d80-8cb8-8777321a8b2a",
		"x-ct-cs-digitink": "bff91361-f865-4a4a-8960-1a7531585524",
		"x-ct-locale": "fr",
		"x-ct-timestamp": "1547739250",
		"x-ct-version": "a93f675d7029d79cb5be740a8d285b2600777251",
		"x-not-a-bot": "i-am-human",
		"x-requested-with": "XMLHttpRequest",
		"x-user-agent": "CaptainTrain/1547739250(web) (Ember 3.4.6)"
	},
	"referrer": "https://www.trainline.fr/cart/pay",
	"referrerPolicy": "no-referrer-when-downgrade",
	"body":
	{
		"payment":
		{
			"mean": "free",
			"cents": 0,
			"currency": "EUR",
			"holder": null,
			"number": null,
			"expiration_month": null,
			"expiration_year": null,
			"cvv_code": null,
			"nonce": null,
			"paypal_email": null,
			"paypal_first_name": null,
			"paypal_last_name": null,
			"paypal_country": null,
			"device_data": null,
			"status": "waiting_for_confirmation",
			"verification_form": null,
			"verification_url": null,
			"can_save_payment_card": false,
			"is_new_customer": false,
			"digitink_value": null,
			"pnr_ids": ["32449277"],
			"after_sales_charge_ids": [],
			"subscription_ids": [],
			"exchange_ids": [],
			"coupon_ids": [],
			"order_id": null,
			"payment_card_id": null,
			"wants_all_marketing": null
		}
	},
	"method": "POST",
	"mode": "cors"
});

// RESPONSE HEADERS
"access-control-allow-methods: GET, POST, PUT, DELETE, HEAD"
"access-control-allow-origin: https://www.trainline.fr"
"access-control-expose-headers: X-CT-Status, X-Request-Id, X-CT-Timestamp"
"access-control-max-age: 1728000"
"cache-control: max-age=0, private, must-revalidate"
"content-encoding: gzip"
"content-language: fr"
"content-length: 2445"
"content-type: application/json"
"date: Sun, 20 Jan 2019 15:18:42 GMT"
"set-cookie: bm_sv=8C5F123FF7C3526B48A347E878DA8CF3~6fp70eSS2qDCP/YlUoxPf+uQwID7IYWXZHd/rl/ieKBtsLFWBVBKTMLkkDbAxM8gIdILmIp/Dmkkx79ZEAx/OVyCde7h/Qu94mK+F3YtkTYgbDTtsRsAkUkXyJjAajGlIHSzQ1iaNPO2j3CQ5lBy9/gFz9FraOjDFEW2FEvji0c=; Domain=.trainline.fr; Path=/; Max-Age=5602; HttpOnly"
"status: 200"
"strict-transport-security: max-age=16070400"
"vary: Accept-Encoding"
"vary: Origin"
"x-ct-status: OK"
"x-recruitment: Cool jobs available @ https://www.trainline.eu/jobs"
"x-request-id: 16a1a7be1f1a32e104f3dc6cd491ef9e"
"x-runtime: 0.554797"
"x-tltokeniser: true"


// RESPONSE BODY
var confirm_response_body = {
	"pnrs": [
	{
		"id": "32449277",
		"after_sale_url": "",
		"alterable_passengers_parts": [],
		"booking_status": "booked",
		"cents": 0,
		"currency": "EUR",
		"exchangeable_parts": [],
		"formatted_instructions":
		{
			"primary": "E-billet nominatif \u003cb\u003eUDWWRO\u003c/b\u003e stocké dans la carte Voyageur. Voyage \u003cmark\u003eà confirmer 48 h avant le départ\u003c/mark\u003e sur \u003ca href=\"https://www.tgvmax.fr/trainline/fr-FR/\" target=\"_blank\"\u003el’Espace Max\u003c/a\u003e, sans quoi le billet sera automatiquement annulé."
		},
		"is_printed": false,
		"local_amount":
		{
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
		"terms_of_transportation": ["sncf"],
		"invoice_available": false,
		"is_paid": true,
		"is_quarantined": false,
		"is_emission_in_progress": true,
		"needs_identification": false,
		"needs_refresh": true,
		"is_classic": false,
		"is_eticket": true,
		"is_mticket": true,
		"is_ticketless": false,
		"is_emitted": false,
		"reservation_name": "WATERLOT",
		"hide_ticket_time_limit": false,
		"ticket_time_limit": null,
		"safe_ticket_time_limit": "2019-01-22T06:20:00+01:00",
		"proof_ids": [],
		"after_sales_log_ids": [],
		"booker_id": "570318",
		"folder_ids": ["56304142"],
		"group_id": "vevqaoslmsngnf",
		"user_id": "570318",
		"order_id": null,
		"travel_document_ids": [],
		"mgmt_info_captured_values": []
	}],
	"folders": [
	{
		"id": "56304142",
		"arrival_date": "2019-01-29T09:15:00+01:00",
		"cents": 0,
		"currency": "EUR",
		"departure_date": "2019-01-29T06:25:00+01:00",
		"digest": "3b358f8bb4a39aa37426643509a4f34572012569",
		"direction": "outward",
		"local_amount":
		{
			"subunit": 0,
			"subunit_to_unit": 100
		},
		"local_currency": "EUR",
		"system": "pao_sncf",
		"arrival_station_id": "4924",
		"departure_station_id": "1339",
		"pnr_id": "32449277",
		"trip_ids": ["76199868"]
	}],
	"trips": [
	{
		"id": "76199868",
		"arrival_date": "2019-01-29T09:15:00+01:00",
		"cents": 0,
		"currency": "EUR",
		"departure_date": "2019-01-29T06:25:00+01:00",
		"local_amount":
		{
			"subunit": 0,
			"subunit_to_unit": 100
		},
		"local_currency": "EUR",
		"arrival_station_id": "4924",
		"departure_station_id": "1339",
		"folder_id": "56304142",
		"passenger_id": "3d039552-ffe4-4ece-9384-c91f242b8b39",
		"segment_ids": ["94572787"]
	}],
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
			"seating.lower_deck":
			{}
		},
		{
			"seating.twin":
			{}
		},
		{
			"seating.aisle":
			{
				"count": 1,
				"pluralization_key": "one"
			}
		}],
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
	}],
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
		}]
	}],
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
	}],
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
	}],
	"proofs": [],
	"participants": [
	{
		"id": "570318",
		"first_name": "Benjamin",
		"last_name": "Waterlot",
		"gender": "male",
		"user_id": "570318"
	}],
	"after_sales_logs": [],
	"travel_documents": [],
	"meta":
	{},
	"orders": [],
	"payment":
	{
		"id": "17527204",
		"status": "success",
		"can_save_payment_card": false,
		"cents": 0,
		"currency": "EUR",
		"local_amount":
		{
			"subunit": 0,
			"subunit_to_unit": 100
		},
		"local_currency": "EUR",
		"transactions": [
		{
			"system": "ct",
			"status": "success",
			"cents": 0,
			"currency": "EUR"
		}],
		"is_new_customer": false,
		"exchange_ids": [],
		"pnr_ids": ["32449277"],
		"subscription_ids": [],
		"after_sales_charge_ids": [],
		"coupon_ids": []
	},
	"coupons": [],
	"user":
	{
		"id": "570318",
		"comfort_filter": "low",
		"first_name": "Benjamin",
		"flexibility_filter": "nonflexi",
		"last_name": "Waterlot",
		"locale": "fr",
		"oldest_departure_date": "2014-12-25T16:41:00+01:00",
		"preferred_currency": null,
		"profile_picture_url": "https://graph.facebook.com/v2.10/10204704567124768/picture?return_ssl_resources=1",
		"third_party_id": "fdc3c58f33f9a03b5c8657d63304015bd0517cf5",
		"migrated": null,
		"email": "benjamin.waterlot@grenoble-em.com",
		"is_concur": false,
		"is_confirmed": true,
		"authentication_schemes": ["password",
			"facebook"
		],
		"permissions": [],
		"settings":
		{
			"onboarding_frontend15_welcome": true,
			"onboarding_trainline_welcome": true
		},
		"signup_referral": null,
		"suggested_travels": [
			["1339",
				"4916"
			],
			["4916",
				"1339"
			],
			["4916",
				"659"
			],
			["1339",
				"3358"
			],
			["4916",
				"5745"
			],
			["4718",
				"4916"
			]
		],
		"wants_ics": true,
		"wants_newsletter": true,
		"wants_all_marketing": null,
		"wants_passbook": true,
		"wants_proof_of_travel": false,
		"wants_carrier_invoice": null,
		"uses_mobile_apps": true,
		"promote_mobile_apps": false,
		"calendar_public_url": null,
		"address_id": null,
		"billing_address_id": null,
		"concur_id": null,
		"identification_document_ids": ["1f75e63f-ce5e-40d6-adda-bfcf89802776"],
		"passenger_ids": ["8410601",
			"6806966"
		],
		"suggested_station_ids": ["1339",
			"4916",
			"659",
			"3358",
			"5745",
			"4718",
			"8267",
			"4652",
			"827",
			"153",
			"4791"
		]
	}
}