import pyperclip
import os


FILE_NAME = "passwords.text"

def save_password():
    website = input("Enter the website name: ")
    password = input("Enter the password: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{website} <|||> {password}\n")
    print(f"Password for {website} saved successfully.")

def get_password():
    website = input("Enter website name to retrieve password: ")

    with open(FILE_NAME, "r") as f:
        for line in f:
            if website in line:
                password = line.split("<|||>")[1].strip()
                pyperclip.copy(password)
                print(f"Password for {website} copied to clipboard.")
                break
            else:
                print(f"No password found for {website}.")
                break

def main():
    while True:
        print("1. Save password")
        print("2. Get password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Exiting the program.")   
            break
        else:
            print("Invalid choice. Please try again.")


main()