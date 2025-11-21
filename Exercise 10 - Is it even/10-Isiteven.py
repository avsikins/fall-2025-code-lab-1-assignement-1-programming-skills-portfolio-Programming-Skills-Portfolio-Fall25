# Exercise 10: Is it even?
# This program checks if a number entered by the user is even or odd.

def check(number): 
    if number % 2 == 0:
        return (f"{number} is even.")
    else:
        return (f"{number} is odd.")

# Main function to execute the program
def main(): 
    digit = int(input("Enter a number: ")) 
    result = check(digit)
    print(result)

main() 