import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/updates/'


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        print(obj['id'])
        if obj['id'] == 1:
            r = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r.json())
    return data


get_list()
