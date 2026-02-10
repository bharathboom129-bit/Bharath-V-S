# Ask the user for a filename
filename = input("Enter the filename to open: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)

except FileNotFoundError:
    # Friendly error message
    print("Oops! That file doesn't exist yet.")
