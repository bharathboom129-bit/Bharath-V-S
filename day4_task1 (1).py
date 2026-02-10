# Step 1: Create a dictionary with three contacts
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9988776655"
}

# Step 2: Add a new contact
contacts["Diana"] = "9001122334"

# Step 3: Update an existing contact
contacts["Bob"] = "9112233445"

# Step 4: Safe access using .get()
print("Lookup Results:")
print("Alice:", contacts.get("Alice", "Contact not found"))
print("Eve:", contacts.get("Eve", "Contact not found"))

print("\nContact List:")
# Step 5: Iterate through contacts
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
