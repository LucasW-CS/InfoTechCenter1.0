import sys
import time  # Importing time module for sleep functionality

# Print a welcome message
print("\nWelcome to InfoTechCenter V1.0\n")

x = 0  # Initialize a counter variable
ellipsis = 0  # Initialize ellipsis counter to control the number of dots in the booting message

# Start a while loop that runs until x equals 20
while x != 20:
    x += 1  # Increment the counter
    # Create a message with an increasing number of dots
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the number of dots
    sys.stdout.write("\r" + message)  # Use sys.stdout.write to update the message in place
    time.sleep(.5)  # Pause for 0.5 seconds to simulate a loading effect
    if ellipsis == 4:  # Reset ellipsis after 3 dots (when it reaches 4)
        ellipsis = 0
    if x == 20:  # When the counter reaches 20, print the final message
        print("\n\nOperating System Booted up - Retina Scanned - Access Granted")
