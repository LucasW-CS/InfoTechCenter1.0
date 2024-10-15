print("\n***********************************************")
import random  # Randomly selects weather condition
from time import sleep  # Used for simulating delays
def weather():
    # Define a list of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)  # Randomly select and return one condition
# Define weather conditions along with the alarm delay and speed limit
weather_conditions = {
    "snowy": {"delay": 30, "speed": 55},
    "blizzard": {"delay": 45, "speed": 45},
    "raining": {"delay": 15, "speed": 65},
    "windy": {"delay": 5, "speed": 70},
    "icy": {"delay": 50, "speed": 30},
}
def vehicleResponseSystem(weatherAlert):
    # Check if the weather condition is in the dictionary
    if weatherAlert in weather_conditions:
        condition = weather_conditions[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {condition['delay']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS system has been engaged only allowing you to drive {condition['speed']}mph.")
    else:
        # If the weather is not in the dictionary (e.g., sunny or other conditions)
        print(f"\nThe National Weather Service is calling for {weatherAlert} skies, drive carefully to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")
# Get a random weather alert
weatherAlert = weather()
# Call the vehicle response system with the selected weather
vehicleResponseSystem(weatherAlert)
