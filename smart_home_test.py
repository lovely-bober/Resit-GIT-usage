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


def set_rgb_color(red, green, blue, brightness=100):
    """
    Set color using RGB values.
    
    Args:
        red (int): Red value (0-255)
        green (int): Green value (0-255) 
        blue (int): Blue value (0-255)
        brightness (int): Brightness level (0-100), default 100
    """
    # Convert RGB to HSV 
    r, g, b = red/255.0, green/255.0, blue/255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val
    
    # Calculate hue
    if diff == 0:
        hue = 0
    elif max_val == r:
        hue = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        hue = (60 * ((b - r) / diff) + 120) % 360
    elif max_val == b:
        hue = (60 * ((r - g) / diff) + 240) % 360
    
    # Calculate saturation
    saturation = 0 if max_val == 0 else (diff / max_val) * 100
    
    change_color(int(hue), int(saturation), brightness)


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