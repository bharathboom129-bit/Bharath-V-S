# Create a tuple for screen resolution
screen_res = (1920, 1080)
# Print current resolution
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
# The Experiment: try to modify the tuple (this will cause an error)
# screen_res[0] = 1280   # Uncomment this line to see the TypeError
# The Fix: explain why it doesn't work
print("Tuples cannot be modified!")
