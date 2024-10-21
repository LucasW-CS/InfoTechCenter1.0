
import sys
import time  # Importing time module for sleep functionality

# ANSI escape codes for coloring text
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
WHITE = '\033[37m'

# Print a welcome message in Blue
print(f"{BLUE}\nWelcome to InfoTechCenter V1.0\n{RESET}")

TimeToSleep = 2  # variable to set the time library to 2 seconds when called
time.sleep(TimeToSleep)  # calling the time to sleep library with the variable TimeToSleep

x = 0  # Initialize a counter variable
ellipsis = 0  # Initialize ellipsis counter to control the number of dots in the booting message

# Start a while loop that runs until x equals 20
while x != 20:
    x += 1  # Increment the counter
    # Create a message with an increasing number of dots
    message = (f"{BLUE}Infotech Center System Booting" + "." * ellipsis + f"{RESET}")
    ellipsis += 1  # Increment the number of dots
    sys.stdout.write("\r" + message)  # Use sys.stdout.write to update the message in place
    time.sleep(0.5)  # Pause for 0.5 seconds to simulate a loading effect
    if ellipsis == 4:  # Reset ellipsis after 3 dots (when it reaches 4)
        ellipsis = 0
    if x == 20:  # When the counter reaches 20, print the final message
        print(f"\n\n{BLUE}Operating System Booted up - Retina Scanned - Access Granted{RESET}")

print("\n***********************************************")
print("Weather Branch")
# Prints a separator line of asterisks to visually structure the output

import random  # Randomly selects weather condition
from time import sleep  # Used for simulating delays

def weather():
    # Define a list of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)  # Randomly select and return one condition

# Dictionary that maps weather conditions to their alarm delay (minutes) and vehicle speed (mph)
weather_conditions = {
    "snowy": {"delay": 30, "speed": 55},
    "blizzard": {"delay": 45, "speed": 45},
    "raining": {"delay": 15, "speed": 65},
    "windy": {"delay": 5, "speed": 70},
    "icy": {"delay": 50, "speed": 30},
}

def vehicleResponseSystem(weatherAlert):
    # Check if the weather condition exists in the weather_conditions dictionary
    if weatherAlert in weather_conditions:
        # Retrieve the corresponding delay and speed for the current weather condition
        condition = weather_conditions[weatherAlert]
        # Display the alarm delay message based on the weather condition
        print(f"\nThe National Weather Service has updated our alarm by {condition['delay']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)  # Simulate a 1-second delay to mimic processing
        # Display the vehicle's speed adjustment based on the weather condition
        print(f"\nVRS system has been engaged only allowing you to drive {condition['speed']}mph.")
    else:
        # For weather conditions not in the dictionary (e.g., "sunny"), print a default message
        print(f"\nThe National Weather Service is calling for {weatherAlert} skies, drive carefully to your destination!")
        sleep(1)  # Simulate a 1-second delay
        # Indicate that the VRS system has been disengaged
        print("\nVRS system has been disengaged.")

# Get a random weather alert by calling the weather function
weatherAlert = weather()

# Call the vehicleResponseSystem function, passing in the randomly selected weather condition
vehicleResponseSystem(weatherAlert)

