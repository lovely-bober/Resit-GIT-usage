import requests

domoticz_url = "http://127.0.0.1:8080/json.htm"
idx = 4 # id number in domoticz
command = input("On or Off: ").strip().capitalize()

# parameters for the switching on and off
params = {
    "type": "command",
    "param": "switchlight",
    "idx": idx,
    "switchcmd": command
}

auth = ('admin', 'domoticz') # username and password for authentication/login in

response = requests.get(domoticz_url, params=params, auth=auth)

# printing the response
print("Status code:", response.status_code)
print(response.json())