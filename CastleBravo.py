print("\n***********************************************")
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
