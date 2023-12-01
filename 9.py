print("alifattahi")
#Dictionary containing bread prices
prices = {
    'berberi': 2000,
    'lavash': 1500,
    'baguette': 1800,
    'tufton': 2200,
    'sangg': 2500
}

def nan_program():
    total_cost = 0

    while True:
        print("Available bread models: berberi, lavash, baguette, tufton, sangg")
        bread_type = input("Enter the type of bread you want (or exit to finish):")

        if bread_type == 'exit':
            break

        if bread_type in prices:
            quantity = int(input(f"Enter the number of {bread_type} you want: "))
            cost = prices[bread_type] * quantity
            total_cost += cost
            print(f"The cost of your {bread_type} bread is {cost} tomans.")
        else:
            print("The type of bread entered is not valid. Please try again.")

    print(f"\nTotal cost of your breads: {total_cost} Tomans. Thanks for your purchase!")

# Run the program
nan_program()
