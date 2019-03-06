import requests
import json

data = {
  "Destino": {
    "address": "Antonio varas",
    "ciudad": "santiago",
    "comuna": "providencia",
    "number": "880",
    "pais": "chile"
  },
  "Inicio": {
    "address": "apoquindo",
    "ciudad": "santiago",
    "comuna": "las condes",
    "number": "4820",
    "pais": "chile"
  }
}

headers = {'Content-Type': 'application/json'}

r = requests.post("http://18.234.35.88:32668/get_latlon", data=json.dumps(data), headers=headers)
h = requests.post("http://18.234.35.88:32234/get_time", data=r, headers=headers) #uber
 #google

print(h.json())
