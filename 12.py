# Dictionary of bread types and their prices
prices = {
    "Barbari": 1000,
    "Lavash": 1500,
    "Baguette": 2000,
    "TafTon": 2500,
    "Sangak": 3000
}

# Function to calculate the total number of bread loaves
def calculate_total_loaves(order):
    total_loaves = 0
    
    # Loop to calculate the total number of loaves for each bread type
    for bread, quantity in order.items():
        total_loaves += quantity
    
    return total_loaves

# Empty dictionary to store the bread order
order = {}

# Loop to ask for the bread type and quantity
while True:
    bread_type = input("Please enter the type of bread you want (Enter nothing to stop): ")
    
    # If the user doesn't enter a bread type, break the loop
    if bread_type == "":
        break
    
    quantity = int(input(f"Please enter the quantity of {bread_type} you want: "))
    
    # Add the bread type and quantity to the order
    order[bread_type] = quantity

# Calculate the total number of bread loaves
total_loaves = calculate_total_loaves(order)

# Display the total number of bread loaves
print(f"You ordered a total of {total_loaves} loaves of bread.")
