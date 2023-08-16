# Basic Greeting
# Commenting
# Creating Functions
# Menu Loop
# Condition for Menu Selection
# Receiving User Input
# Validating User Input
# Error Handling
# Calculating the values
# Exiting Program

def main():
    name = greeting()
    get_menu()
    goodbye(name)

def greeting():
    print("\nWelcome to Python Learning!")
    name = input("\nWhat is your name? ")
    print(f"Hello {name}! You can start by selecting the below menu.")
    return name

def goodbye(name):
    print(f"\nProgram exit now... Goodbye {name}!\n")

def get_menu():    
    while True:
        print("\n-- Program Menu --")        
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Calculate area of Rectangle")
        print("0. Exit Program")

        try:
            selectedmenu = int(input("\nSelect menu for action: "))
            if selectedmenu == 1:
                convert_fahrenheit()
            elif selectedmenu == 2:            
                convert_celsius()
            elif selectedmenu == 3:
                calculate_area_rectangle()
            elif selectedmenu == 0:
                # print("Program Exit....\n")
                False
                break
            else:
                print("Selected menu out of range, please try again.")              
        except ValueError:
            print("Selected menu is invalid, please try again.")

def convert_celsius():
    try:
        f = int(input("Enter Fahrenheit value: "))
        return print((f - 32) * 5/9)
    except ValueError:
        print("Input value of Fahrenheit is invalid, please provide correct value.")
        pass
        

def convert_fahrenheit():
    try:
        c = int(input("Enter Celsius value: "))    
        return print((c * 9/5) + 32)
    except ValueError:
        print("Input value of Celsius is invalid, please provide correct value")
        pass

def calculate_area_rectangle():
    try:
        # area = int(input("Length: ")) * int(input("Height: "))
        length = input("Length: ")
        length = int(length)
        height = input("Height: ")
        height = int(height)
        return print("Area of Rectangle: ", length * height)
    except ValueError:
        print(f"Input value of length {length} and height {height} in which input value is not valid for caculation!")        
        pass

main()