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
