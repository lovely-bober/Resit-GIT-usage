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

def change_color(hue, saturation, brightness=100):
    """
    Change the color of Philips Hue lamp.
    
    Args:
        hue (int): Color hue (0-360)
        saturation (int): Color saturation (0-100)
        brightness (int): Brightness level (0-100), default 100
    """
    params = {
        "type": "command",
        "param": "setcolbrightnessvalue",
        "idx": idx,
        "hue": int(hue),
        "brightness": int(brightness),
        "saturation": int(saturation),
        "iswhite": "false"
    }

    response = requests.get(domoticz_url, params=params, auth=auth)
    
    print("Status code:", response.status_code)
    print(response.json())

