import requests

domoticz_url = "http://127.0.0.1:8080/json.htm"
idx = 4
command = input("On or Off: ").strip().capitalize()

params = {
    "type": "command",
    "param": "switchlight",
    "idx": idx,
    "switchcmd": command
}

auth = ('admin', 'domoticz') 

response = requests.get(domoticz_url, params=params, auth=auth)

print("Status code:", response.status_code)
print(response.json())