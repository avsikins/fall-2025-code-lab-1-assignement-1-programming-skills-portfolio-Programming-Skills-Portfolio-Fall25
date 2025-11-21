# Exercise 03: Biography
# This program collects and displays a user's name, hometown, and age.

def valid_age():
    while True:
        age_input = input("Enter your age: ")
        # Validates that the input is an integer
        try:
            return int(age_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer for your age.")
 
# Main function to collect user information
def main():
    name = input("Enter your name: ") 
    hometown = input("Enter your hometown: ")
    age = valid_age() 
    # Returns user information as a dictionary
    return {
        "Name": name,
        "Hometown": hometown,
        "Age": age
    }

if __name__ == "__main__":
    bio = main() 
    # Prints each piece of information on a separate line
    print(bio["Name"], bio["Hometown"], bio["Age"], sep="\n")