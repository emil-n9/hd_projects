
#========The Shoe class==========
class Shoe:

    #initialisation method
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    #Method returns the cost of the shoe
    def get_cost(self):
        print("The shoes cost:", self.cost)

    #Method returns quantity of the shoe
    def get_quantity(self):
        print("There are", self.quantity, "pairs of this shoe")

    #String representation of the object containing all the information
    def __str__(self):
        print(f"The {self.product}, code: {self.code} is manufactured in {self.country}. There are {self.quantity} pairs of this shoe, each costing {self.cost}.\n")


#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============

#Reads lines from the inventory.txt file and creates a shoe object for each which is then added to the shoe list
def read_shoes_data():
    with open('inventory.txt', 'r') as f:
        contents = f.readlines()
        enumerate(contents)
        for i in range(1, len(contents)):
            attributes = contents[i].split(",")
            shoe_list.append(Shoe(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4]))

#Creates a new shoe object and adds it to the shoe list      
def capture_shoes():
    country = input("Enter the country in which the shoe is manufactured: ")
    code = input("Enter the code for the shoe: ")
    product = input("Enter the name of the shoe: ")
    
    while True:
        try:
            cost = int(input("Enter the cost of the shoe: "))
            break
        except ValueError:
            print("Invalid input, please try again.")
    
    while True:
        try:
            quantity = int(input("Enter the quantity of the shoe: "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    shoe_list.append(Shoe(country, code, product, cost, quantity))
    
#Prints the string representation of each object in the shoe list
def view_all():
    for i in range(0, len(shoe_list)):
        shoe_list[i].__str__()

#Finds the shoe with the lowest quantity and ask user if they'd like to add to that amount
def re_stock():
    quantity_list = []
    for i in range(0, len(shoe_list)):
        quantity_list.append(int(shoe_list[i].quantity))
    
    lowest = min(quantity_list)
    lowest_index = quantity_list.index(lowest)

    add_to = input(f"\nThere are only {lowest} pairs of the {shoe_list[lowest_index].product}. Would you like to add to this amount? (y/n): ")
    
    while True:
        if add_to.lower() == "y":
            while True:
                try:
                    quantity_add = int(input("How many pairs would you like to add?: "))
                    break
                except ValueError:
                    print("Invalid input, please try again.")
            break
        elif add_to.lower() == "n":
            exit()
        else:
            print("Invalid input, please try again.")
            add_to = input(f"There are only {lowest} pairs of the {shoe_list[lowest_index].product}. Would you like to add to this amount? (y/n): ")
        
    #Updates the inventory.txt file with the new quantity
    with open('inventory.txt', 'r') as f:
        contents = f.readlines()
        enumerate(contents)
        contents[lowest_index + 1] = f"{shoe_list[lowest_index].country},{shoe_list[lowest_index].code},{shoe_list[lowest_index].product},{shoe_list[lowest_index].cost},{lowest + quantity_add}\n"
    
    with open('inventory.txt', 'w') as f2:
        for line in contents:
            f2.write(line)

    #Calls read_shoes_data method to update the shoe list
    read_shoes_data()

#Returns the string represenation of the shoe object with the matching code
def search_shoe():
    shoe_code = input("Enter the code of the shoe you are searching for: ")

    found = False
    for i in range(0, len(shoe_list)):
        if shoe_list[i].code == shoe_code:
            shoe_list[i].__str__()
            found = True
    
    if not found:
        print("A shoe with this code was not found.")

#Returns the value of each shoe
def value_per_item():
    for i in range(0, len(shoe_list)):
        value = int(shoe_list[i].cost) * int(shoe_list[i].quantity)
        print(f"The value of {shoe_list[i].product} is {value}")

#Returns the shoe with the highest quantity 
def highest_qty():
    quantity_list = []
    for i in range(0, len(shoe_list)):
        quantity_list.append(int(shoe_list[i].quantity))
    
    highest = max(quantity_list)
    highest_index = quantity_list.index(highest)

    print(f"There are {highest} pairs of the {shoe_list[highest_index].product} and it is on sale.")

#==========Main Menu=============
while True:
    menu = input('''Select one of the following Options below:
r - Read data from the inventory file
c - Capture data about a shoe
va - View all shoes
r - Restock shoe with lowest quantity
s - Search for a specific shoe using the shoe code
v - Returns the value of each shoe
h - Returns the shoe with the highest quantity 
e - Exit
: ''').lower()
    if menu == "r":
        read_shoes_data()
    elif menu == "c":
        capture_shoes()
    elif menu == "va":
        view_all()
    elif menu == "r":
        re_stock()
    elif menu == "s":
        search_shoe()
    elif menu == "v":
        value_per_item()
    elif menu == "h":
        highest_qty()
    elif menu == "e":
        exit()
    else:
        print("Wrong input, please try again.")