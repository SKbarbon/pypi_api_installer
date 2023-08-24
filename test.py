import requests, json


URL = f"https://pypi.org/pypi/requests/json"

r = requests.get(URL).text
r = json.loads(r)

for i in r['info']['requires_dist']:
    print(i)