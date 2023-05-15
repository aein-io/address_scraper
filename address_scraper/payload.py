url = "https://realty-in-us.p.rapidapi.com/properties/v3/list"

payload = {
    "limit": 200,
    "offset": 0,
    "baths": {"min": 3},
    "list_price": {
        "max": 900,
        "min": 200
    },
    "beds": {
        "max": 3,
        "min": 1
    },
    "cats": True,
    "dogs": True,
    "state_code": "TX",
    "status": ["for_rent"],
    "type": [
        "condos",
        "condo_townhome_rowhome_coop",
        "condo_townhome",
        "townhomes",
        "duplex_triplex",
        "single_family",
        "multi_family",
        "apartment",
        "condop",
        "coop"
    ],
    "sort": {
        "direction": "desc",
        "field": "list_date"
    }
}


headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "66b9b90781mshe91a7e9a268d871p1d685ejsn383619a1186e",
    "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
}
