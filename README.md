# Resit-GIT-usage
New GIT repository for the resit on the 4th of July 

Smart Home Integration: Domoticz & Philips Hue
This repository contains Python scripts for controlling Philips Hue lamps via the Domoticz home automation platform. It demonstrates how to interact with Domoticz’s API to switch Hue lights on/off and change their color/brightness.

Overview
Purpose: Automate and control Philips Hue lamps using Domoticz.

- Switch the light on or off

- Set the light color using HSV (Hue, Saturation, Value)

- Set the light color using RGB (Red, Green, Blue)

- Set the light color by common color name (e.g., "red", "blue", "orange")

Features:
- Easy Color Control: Choose colors using HSV, RGB, or by name.

- Brightness Adjustment: Set brightness level (0-100).

- Simple On/Off: Quickly toggle the light.

- Built-in Color Names: Use common names for quick color changes.

- Technology Stack: Python, Domoticz, Philips Hue.

Requirements:
- Python 3.x

- requests library (pip install requests)

- A running Domoticz server (default URL: http://127.0.0.1:8080)

- The device index (idx) of your Philips Hue or compatible light in Domoticz

Customization
- Add More Colors: Edit the COLOR_RGB dictionary to add more named colors.

- Change Device: Update the idx variable for a different light.

Troubleshooting
- Connection errors: Ensure Domoticz is running and accessible at the specified URL.

- Authentication errors: Double-check your username and password.

- Light not responding: Ensure the correct idx is set for your device.
