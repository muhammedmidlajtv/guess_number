import random

def rolldice(a,b):

    num = random.randint(a, b)
    return num

def main():
    print("\t\t\t😃😃😃😃😃 WELCOME 😃😃😃😃😃\t\t\t")
    print('Enter the limit lower limit and upper limit of numbers to be guessed:')
    a = int(input())
    b = int(input())
    val = rolldice(a,b)
    while 1:
        option = int(input("Guess the number\n"))
        if option == val:
            print(' Your Guessed number is correct\n')
            break
        elif option != val:
            print('sorry its wrong😕\nTry one more😃')
            continue
        else:
            print("Invalid option 😕")

    print("Thank you for playing , Have a nice day 🌞")


main()
