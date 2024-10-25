import sys
import time  # Importing time module for sleep functionality
import random  # Randomly selects weather condition
from time import sleep  # Used for simulating delays


print("\n***********************************************")
print("Gasoline Branch")
# Prints a separator line of asterisks to visually structure the output





# Function to simulate gas level indicator
def gasLevelGauge():
    # List of possible gas levels
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to simulate available gas stations
def gasStations():
    # List of possible gas station names
    return random.choice(["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"])


# Function to alert the driver about their gas level
def gasLevelAlert():
    # Get the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Dictionary to store gas levels and corresponding distances
    distanceRanges = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }


    # Messages and logic for different gas levels
    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")




    elif gasLevelIndicator in ["Low", "Quarter Tank"]:
        print(f"Your gas tank is {gasLevelIndicator.lower()}, checking GPS for the closest gas station.")
        sleep(2)
        # Get distance to the nearest gas station based on the gas level
        milesToGasStation = distanceRanges.get(gasLevelIndicator, 0)
        print(f"The closest gas station is {gasStations()} which is {milesToGasStation} miles away.")

    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination.")

    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")

    else:
        print("Your gas tank is full!!! Vroom Vroom")




# Call the gasLevelAlert function to run the gas level alert system
gasLevelAlert()





