import requests, json


URL = f"https://pypi.org/pypi/googletrans/json"

r = requests.get(URL).text
r = json.loads(r)
print(r['info'])
for i in r['info']['requires_dist']:
    print(i)