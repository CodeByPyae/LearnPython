# Simple Calculator Program with Two Input Values

def main():
    operations()

def menu():
    print("")
    print(".-- Calculator Program --.")
    print("| 1. Add                 |")
    print("| 2. Substract           |")
    print("| 3. Multiply            |")
    print("| 4. Divide              |")
    print("| 5. Modulus             |")
    print("| 6. Power               |")
    print("| 0. Exit Program        |")
    print(";------------------------;")    
    
def operations():
    menu()
    while True:        
        try:
            selectedmenu = int(input("\nSelect menu for operation."))
            
            if selectedmenu == 0:
                print("Program Exit....\n")
                False
                break
            elif selectedmenu > 6 or selectedmenu < 0:
                print("Invalid menu selection, please try again")
                pass
            else:
                while True:
                    try:
                        x = int(input("Number 1: "))                        
                        False
                        break    
                    except ValueError:
                        print("Invalid input. Please enter number.")

                while True:
                    try:                        
                        y = int(input("Number 2: "))                
                        False
                        break    
                    except ValueError:
                        print("Invalid input. Please enter number.")

                if selectedmenu == 1:
                    add(x, y)
                elif selectedmenu == 2:
                    substract(x, y)
                elif selectedmenu == 3:
                    multiply(x, y)
                elif selectedmenu == 4:
                    if y == 0:
                        print("Division by zero is invalid!")                        
                    else:
                        divide(x, y)
                elif selectedmenu == 5:
                    if y == 0:
                        print("Division by zero is invalid!")                        
                    else:
                        modulus(x, y)
                elif selectedmenu == 6:
                    power(x, y)                
                else:
                    print("Invalid menu selection, please try again!")           
                    break

        except ValueError:
            print("Invalid menu selection, please try again")            

def add(x, y):
    return print(f"{x} + {y} = {x + y}")

def substract(x, y):
    return print(f"{x} - {y} = {x - y}")

def multiply(x, y):
    return print(f"{x} * {y} = {x * y}")

def divide(x, y):    
    return print(f"{x} / {y} = {x / y}")

def modulus(x, y):
    return print(f"{x} % {y} = {x % y}")

def power(x, y):
    # Exponential operator **, 2**5 = 2*2*2*2*2
    return print(f"{x} ^ {y} = {x ** y}")
    
main()