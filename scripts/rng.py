import random

while True:
    x = input("Out of: ")
    
    if x == '':
        print("Exiting...")
        break
    
    try:
        result = random.randint(1, int(x))
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number.")
