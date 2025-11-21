# Exercise 06: Brute Force Attack
# This program simulates a brute force attack by allowing the user to guess a password
# within a limited number of attempts.

password = 12345
attempts = 5

# Loop until the user runs out of attempts
while attempts > 0: 
    guess = int(input("Enter your password guess: ")) 
    if guess == password:
        print("Access Granted.") 
        break 
    else:
        attempts -= 1 
        print(f"Access Denied. You have {attempts} attempts left.")
        if attempts == 0: 
            print("Access Denied. Authorities have been notified.")