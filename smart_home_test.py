# Import the requests library to make HTTP requests
import requests

# Define the base URL for the Domoticz server API
domoticz_url = "http://127.0.0.1:8080/json.htm"

# Specify the device ID (idx) in Domoticz that you want to control
idx = 4  # id number in domoticz

# Set the authentication credentials (username and password)
auth = ('admin', 'domoticz')  # username and password for authentication/login


def light_switch(command):
    """
    Turn light on or off.
    
    Args:
        command (str): "On" or "Off"
    """
    
    # parameters for the switching on and off
    params = {
        "type": "command",                                    # Specifies the action type
        "param": "switchlight",                               # Indicates to switch the light
        "idx": idx,                                           # Device ID to control
        "switchcmd": command.strip().capitalize()             # Command to send (On or Off)
    }

    # Send the HTTP GET request to Domoticz to switch the device
    response = requests.get(domoticz_url, params=params, auth=auth)
    
    # Print the response status code and JSON content for debugging
    print("Status code:", response.status_code)
    print(response.json())
    

def change_color(hue, saturation, brightness=100):
    """
    Change the color of Philips Hue lamp.
    
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

def main():
    print("Color Control Options:")
    print("1. HSV (Hue, Saturation, Value)")
    print("2. Turn light on or off")

    choice = input("Choose option (1/2): ")
    
    if choice == "1":
        hue = input("Hue (0-360): ")
        saturation = input("Saturation (0-100): ")
        brightness = input("Brightness (0-100): ")
        change_color(hue, saturation, brightness)
    elif choice == "2":
        command = input("On or Off: ")
        light_switch(command)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()