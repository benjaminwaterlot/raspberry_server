fetch("https://www.trainline.fr/api/v5_1/search", {
    "credentials": "include",
    "headers": {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "fr-FR,fr;q=0.8",
        "authorization": "Token token=\"7-H-BwKjNL7dmUpfMxMu\"",
        "content-type": "application/json; charset=UTF-8",
        "x-ct-client-id": "129b80ba-d677-4842-a30f-72ad5b1ba8e1",
        "x-ct-locale": "fr",
        "x-ct-timestamp": "1547739250",
        "x-ct-version": "a93f675d7029d79cb5be740a8d285b2600777251",
        "x-not-a-bot": "i-am-human",
        "x-requested-with": "XMLHttpRequest",
        "x-user-agent": "CaptainTrain/1547739250(web) (Ember 3.4.6)"
    },
    "referrer": "https://www.trainline.fr/search",
    "referrerPolicy": "no-referrer-when-downgrade",
    "body": "{\"search\":{\"departure_date\":\"2019-02-08T08:00:00UTC\",\"return_date\":null,\"cuis\":{},\"systems\":[\"sncf\",\"db\",\"idtgv\",\"ouigo\",\"trenitalia\",\"ntv\",\"hkx\",\"renfe\",\"cff\",\"benerail\",\"ocebo\",\"westbahn\",\"leoexpress\",\"locomore\",\"busbud\",\"flixbus\",\"distribusion\",\"cityairporttrain\",\"obb\",\"timetable\"],\"exchangeable_part\":null,\"source\":null,\"is_previous_available\":false,\"is_next_available\":false,\"departure_station_id\":\"1339\",\"via_station_id\":null,\"arrival_station_id\":\"4916\",\"exchangeable_pnr_id\":null,\"passenger_ids\":[\"6806966\"],\"card_ids\":[\"690739\",\"977054\",\"1649967\"]}}",
    "method": "POST",
    "mode": "cors"
});