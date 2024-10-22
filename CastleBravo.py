# Print a decorative line to separate the output
print("\n************************************************\n")

# Print a message indicating the Gasoline Branch section
print("Gasoline Branch\n")

# Importing the 'random' module to generate random choices and 'sleep' from 'time' to pause execution
import random
from time import sleep


# Function to simulate gas level indicator
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly choose one gas level from the list
    return random.choice(gasLevelList)


# Function to simulate available gas stations
def gasStations():
    # List of possible gas station names
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose one gas station from the list
    return random.choice(gasStationsList)


# Function to alert the driver about their gas level
def gasLevelAlert():
    # Random miles to gas station if gas level is low (1 to 25 miles)
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Random miles to gas station if gas level is at a quarter tank (25.1 to 50 miles)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
    # Get the current gas level by calling the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Conditional statements to handle different gas levels
    if gasLevelIndicator == "Empty":
        # Print a warning if the gas level is empty
        print("***WARNING - YOU ARE ON EMPTY***\n")
        # Pause for 2 seconds
        sleep(2)
        # Simulate calling for roadside assistance
        print("Calling Triple AAA")

    elif gasLevelIndicator == "Low":
        # Alert for low gas and check for the nearest gas station
        print("Your gas tank is extremely low, checking GPS for the closest gas station.")
        sleep(2)
        # Display the nearest gas station and distance in miles
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")

    elif gasLevelIndicator == "Quarter Tank":
        # Alert for quarter tank gas level and check for the nearest gas station
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station.")
        sleep(2)
        # Display the nearest gas station and distance in miles
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")

    elif gasLevelIndicator == "Half Tank":
        # Inform the user that half a tank is sufficient
        print("Your gas tank is on half a tank full, which is plenty to get to your destination.")

    elif gasLevelIndicator == "Three Quarter Tank":
        # Inform the user that the gas level is three-quarters full
        print("Your gas tank is on three quarter tank full.")

    else:
        # Inform the user that the gas tank is full
        print("Your gas tank is full!!! Vroom Vroom")


# Call the gasLevelAlert function to run the gas level alert system
gasLevelAlert()
