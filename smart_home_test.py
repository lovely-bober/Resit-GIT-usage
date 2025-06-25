# Import the requests library to make HTTP requests
import requests

# Define the base URL for the Domoticz server API
domoticz_url = "http://127.0.0.1:8080/json.htm"

# Specify the device ID (idx) in Domoticz that you want to control
idx = 4  # id number in domoticz

# Prompt the user to enter the command (On or Off)
command = input("On or Off: ").strip().capitalize()

# Prepare the parameters for switching the device on or off
params = {
    "type": "command",                # Specifies the action type
    "param": "switchlight",           # Indicates to switch the light
    "idx": idx,                       # Device ID to control
    "switchcmd": command              # Command to send (On or Off)
}

# Set the authentication credentials (username and password)
auth = ('admin', 'domoticz')  # username and password for authentication/login

# Send the HTTP GET request to Domoticz to switch the device
response = requests.get(domoticz_url, params=params, auth=auth)

def change_color(hue, saturation, brightness=100):
    """
    Change the color of a Philips Hue lamp (or compatible device) in Domoticz.

    Args:
        hue (int): Color hue (0-360)
        saturation (int): Color saturation (0-100)
        brightness (int): Brightness level (0-100), default 100
    """
    # Prepare the parameters for changing color and brightness
    params = {
        "type": "command",
        "param": "setcolbrightnessvalue",
        "idx": idx,                       # Device ID to control
        "hue": int(hue),                  # Desired hue value
        "brightness": int(brightness),    # Desired brightness value
        "saturation": int(saturation),    # Desired saturation value
        "iswhite": "false"                # Indicates not to use white color mode
    }

    # Send the HTTP GET request to change the color
    response = requests.get(domoticz_url, params=params, auth=auth)
    
    # Print the response status code and JSON content for debugging
    print("Status code:", response.status_code)
    print(response.json())
