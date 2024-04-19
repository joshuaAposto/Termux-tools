import time
import os

def display_menu():
    print("\033[91m")
    print("██╗░░░░░░█████╗░██╗░░░██╗███████╗")
    print("██║░░░░░██╔══██╗██║░░░██║██╔════╝")
    print("██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░")
    print("██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░")
    print("███████╗╚█████╔╝░░╚██╔╝░░███████╗")
    print("╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝")
    print("\033[0m")
    print("\033[91mChoose an option (1, 2, 3, or 0):\033[0m")
    print("1. spam I love you")
    print("2. Option 2")
    print("3. Option 3")
    print("0. Exit")

def spam_love():
    for _ in range(10):
        print("\033[91mI LOVE YOU\033[0m")
        time.sleep(0.5)
    print("\033[91m")
    print("\n………………./´¯/) ")
    print("……………….,/¯../ ")
    print("………………./…./ ")
    print("………./´¯/’…’/´¯¯`·¸ ")
    print("………./’/…/…./……./¨¯\ ")
    print("……..(‘(…´…´…. ¯~/’…’) ")
    print("………\……………..’…./ ")
    print("……….”…\………. _.·´ ")
    print("…………\…………..( ")
    print("…………..\………….\… ")
    print("\033[0m")

def main():
    while True:
        display_menu()
        choice = input("\033[91mChoose an option (1, 2, 3, or 0): \033[0m")
        
        if choice == '1':
            spam_love()
            print("\nThank you for feeling the love!")
        elif choice == '2':
            print("You chose Option 2")
        elif choice == '3':
            print("You chose Option 3")
        elif choice == '0':
            print("Thank you for using! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
        
        # Clear screen
        time.sleep(2)
        os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    main()
