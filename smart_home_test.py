# Import the requests library to handle HTTP requests
import requests

# Dictionary mapping common color names to their RGB values
COLOR_RGB = {
    "red":     (255, 0, 0),
    "green":   (0, 255, 0),
    "blue":    (0, 0, 255),
    "yellow":  (255, 234, 0),
    "cyan":    (0, 255, 255),
    "magenta": (255, 0, 255),
    "pink":    (255, 20, 147),
    "orange":  (255, 165, 0),
    "purple":  (128, 0, 128),
    "white":   (255, 255, 255),
    "black":   (0, 0, 0),
    "gray":    (128, 128, 128),
}

class DomoticzLight:
    """
    Class to control a Domoticz light device via its API.
    """

    def __init__(self, base_url, idx, username, password):
        """
        Initialize the DomoticzLight instance.

        Args:
            base_url (str): The base URL of the Domoticz server.
            idx (int): The device index (ID) in Domoticz.
            username (str): Username for authentication.
            password (str): Password for authentication.
        """
        self.base_url = base_url
        self.idx = idx
        self.auth = (username, password)

    def _send_request(self, params):
        """
        Internal helper to send an HTTP GET request to the Domoticz API.

        Args:
            params (dict): Parameters to include in the request.
        """
        try:
            # Send the request with authentication and a timeout
            response = requests.get(self.base_url, params=params, auth=self.auth, timeout=5)
            response.raise_for_status()  # Raise error if the request failed
            print(f"Status code: {response.status_code}")
            print(response.json())      # Print the parsed JSON response
        except requests.RequestException as e:
            # Print error details if the request fails
            print(f"Request failed: {e}")

    def switch(self, command):
        """
        Turn the light on or off.

        Args:
            command (str): "On" or "Off"
        """
        params = {
            "type": "command",
            "param": "switchlight",
            "idx": self.idx,
            "switchcmd": command.strip().capitalize()  # Ensure correct format
        }
        self._send_request(params)

    def set_color_hsv(self, hue, saturation, brightness=100):
        """
        Set the light color using HSV values.

        Args:
            hue (int): Hue value (0-360)
            saturation (int): Saturation value (0-100)
            brightness (int): Brightness value (0-100), default is 100
        """
        params = {
            "type": "command",
            "param": "setcolbrightnessvalue",
            "idx": self.idx,
            "hue": int(hue),
            "brightness": int(brightness),
            "saturation": int(saturation),
            "iswhite": "false"  # Use color mode, not white mode
        }
        self._send_request(params)

    def set_color_rgb(self, red, green, blue, brightness=100):
        """
        Set the light color using RGB values by converting them to HSV.

        Args:
            red (int): Red value (0-255)
            green (int): Green value (0-255)
            blue (int): Blue value (0-255)
            brightness (int): Brightness value (0-100), default is 100
        """
        # Normalize RGB values to the range [0, 1]
        r, g, b = red / 255.0, green / 255.0, blue / 255.0
        max_val, min_val = max(r, g, b), min(r, g, b)
        diff = max_val - min_val

        # Calculate hue based on which RGB component is the largest
        if diff == 0:
            hue = 0  # Grayscale (no color)
        elif max_val == r:
            hue = (60 * ((g - b) / diff) + 360) % 360
        elif max_val == g:
            hue = (60 * ((b - r) / diff) + 120) % 360
        else:
            hue = (60 * ((r - g) / diff) + 240) % 360

        # Calculate saturation as a percentage
        saturation = 0 if max_val == 0 else (diff / max_val) * 100

        # Set the color using the calculated HSV values
        self.set_color_hsv(int(hue), int(saturation), brightness)

    def set_color_by_name(self, color_name, brightness=100):
        """
        Set the light color using a common color name.

        Args:
            color_name (str): Name of the color (e.g., 'red', 'blue')
            brightness (int): Brightness value (0-100), default is 100
        """
        color_name = color_name.lower()
        if color_name in COLOR_RGB:
            # Look up the RGB values and set the color
            red, green, blue = COLOR_RGB[color_name]
            self.set_color_rgb(red, green, blue, brightness)
        else:
            # Print an error if the color is not recognized
            print(f"Color '{color_name}' not recognized. Available: {', '.join(COLOR_RGB.keys())}")



def main():
    domoticz_url = "http://127.0.0.1:8080/json.htm"
    idx = 4
    username = "admin"
    password = "domoticz"
    light = DomoticzLight(domoticz_url, idx, username, password)

    # Display the available color control options to the user
    print("Color Control Options:")
    print("1. HSV (Hue, Saturation, Value)")
    print("2. RGB (Red, Green, Blue)")
    print("3. Color by name")
    print("4. Turning on and off")

    # Prompt the user to choose one of the options
    choice = input("Choose option (1 - 4): ")
    
    # Option 1: Set color using HSV values
    if choice == "1":
        try:
            hue = int(input("Hue (0-360): "))       # get hue value from user with validation to check if the hue value is between 0 and 360
            if not 0 <= hue <= 360:
                raise ValueError
        except ValueError:
            print("Invalid hue. Please enter a number between 0 and 360.")
            return
        saturation = input("Saturation (0-100): ")  # Get saturation value
        brightness = input("Brightness (0-100): ")  # Get brightness value
        light.change_color(hue, saturation, brightness)   # Call function to apply HSV color
    # Option 2: Set color using RGB values
    elif choice == "2":
        red = input("Red (0-255): ")    # Get red component
        green = input("Green (0-255): ")    # Get green component
        blue = input("Blue (0-255): ")      # Get blue component
        brightness = input("Brightness (0-100): ")  # Get brightness
        light.set_rgb_color(int(red), int(green), int(blue), int(brightness))  # Apply RGB color
    # Option 3: Set color using a color name
    elif choice == "3":
        color_name = input("Color name (e.g. pink, blue, orange): ")    # Ask for color name
        brightness = input("Brightness (0-100): ") # Ask for brightness
        light.set_color_by_name(color_name, int(brightness))  # Set color using the name
    # Option 4: Turn lights on or off
    elif choice == "4":
        command = input("On or Off: ")  # Get command to turn lights on or off
        light.switch(command)   # Call function to switch light
    # If input is invalid
    else:
        print("Invalid choice") # Inform user of invalid input

# Keeps looping so user can do multiple things without having to start the program again
while True:
    if __name__ == "__main__":
        main()
    again = input("Do you want to perform another action? (y/n): ").lower() 
    if again != "y":
        break


