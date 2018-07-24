import core
import disk


def main():
    print('Welcome to the Rental store!')
    user_response = input('Would you like to rent anything?')
    # this is a yes or no question
    if user_response == 'yes':
        print('These is what we have in stock')
        print(inventory)
    elif user_response == 'no':
        print('Thank you have a great day!')
        exit()
    else:
        print('Please choose a valid option!')

    selection = input('Which one would you would like to rent?')
    for selection in inventory:
        if selection in inventory:
            print(selection)


if __name__ == '__main__':
    main()
