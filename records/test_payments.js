// PAYMENTS (Après book, pour réserver)
// REQUETE
fetch("https://www.trainline.fr/api/v5_1/payments",
	{
		"credentials": "include",
		"headers": {
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
				"status": null,
				"verification_form": null,
				"verification_url": null,
				"can_save_payment_card": false,
				"is_new_customer": false,
				"digitink_value": null,
				"pnr_ids": ["32449277"],
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
"content-language: fr"
"content-length: 1498"
"content-type: application/json"
"date: Sun, 20 Jan 2019 15:18:41 GMT"
"set-cookie: bm_sv=8C5F123FF7C3526B48A347E878DA8CF3~6fp70eSS2qDCP/YlUoxPf+uQwID7IYWXZHd/rl/ieKBtsLFWBVBKTMLkkDbAxM8gIdILmIp/Dmkkx79ZEAx/OVyCde7h/Qu94mK+F3YtkTbOWk+zV2m57+MOhGtMwFvyXAIqqirnz3mORmXFYr/ta8pu+S4EuSczkzOhjfgQmns=; Domain=.trainline.fr; Path=/; Max-Age=5603; HttpOnly"
"status: 201"
"strict-transport-security: max-age=16070400"
"vary: Origin"
"x-ct-status: OK"
"x-recruitment: Cool jobs available @ https://www.trainline.eu/jobs"
"x-request-id: f8b57a2d3a61639ea4d37c0674eec4dd"
"x-runtime: 0.254185"
"x-tltokeniser: true"

// RESPONSE_BODY
var confirmation = {
	"meta": {},
	"orders": [],
	"payment":
	{
		"id": "17527204",
		"status": "waiting_for_confirmation",
		"can_save_payment_card": false,
		"exchange_ids": [],
		"pnr_ids": [],
		"subscription_ids": [],
		"after_sales_charge_ids": [],
		"coupon_ids": []
	},
	"coupons": [],
	"user": {
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
			"facebook"],
		"permissions": [],
		"settings": {
			"onboarding_frontend15_welcome": true,
			"onboarding_trainline_welcome": true
		},
		"signup_referral": null,
		"suggested_travels": [["1339", "4916"], ["4916", "1339"], ["4916", "659"], ["1339", "3358"], ["4916", "5745"], ["4718", "4916"]], "wants_ics": true, "wants_newsletter": true, "wants_all_marketing": null, "wants_passbook": true, "wants_proof_of_travel": false, "wants_carrier_invoice": null, "uses_mobile_apps": true, "promote_mobile_apps": false, "calendar_public_url": null, "address_id": null, "billing_address_id": null, "concur_id": null, "identification_document_ids": ["1f75e63f-ce5e-40d6-adda-bfcf89802776"], "passenger_ids": ["8410601", "6806966"], "suggested_station_ids": ["1339", "4916", "659", "3358", "5745", "4718", "8267", "4652", "827", "153", "4791"]
	}
}