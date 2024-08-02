import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

# Run the password generator
main()

