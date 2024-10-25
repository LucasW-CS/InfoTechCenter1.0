import sys
import time  # Importing time module for sleep functionality
import random  # Randomly selects weather condition
from time import sleep  # Used for simulating delays
<<<<<<< Updated upstream
=======

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


>>>>>>> Stashed changes


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



<<<<<<< Updated upstream
# Call the gasLevelAlert function to run the gas level alert system
gasLevelAlert()

=======
>>>>>>> Stashed changes

print("\n***********************************************")
print("Gasoline Branch")



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
<<<<<<< Updated upstream
gasLevelAlert()
>>>>>>> Stashed changes
=======
gasLevelAlert()
>>>>>>> Stashed changes
