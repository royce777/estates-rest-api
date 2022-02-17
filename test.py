import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE+"estates/0", {"name": "Estate Name", "area" : 200, "bedrooms" : 2, "bathrooms" : 2})
print(response.json())
#response = requests.get(BASE+"estates/1")
#print(response.json())