# List of temperature readings
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# First and last readings
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

# Afternoon Peak (4th, 5th, 6th items → index 3 to 5)
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

# Last 3 hours using negative slicing
last_three = temperatures[-3:]
print("Last 3 Hours Readings:", last_three)
