import core
import disk


def main():
    print('Welcome to the Rental store!')
    user_response = input('Would you like to rent anything?')
    # this is a yes or no question
    if user_response == 'yes':
        print('These is what we have in stock')
        with open('inventory.txt') as f:
            inventory = f.readlines()
        print(
            f'{name} in stock:{in_stock} price to rent:{rent} replacement cost:{replacement_value}'
        )
    elif user_response == 'no':
        print('Thank you have a great day!')
        exit()
    else:
        print('Please choose a valid option!')

    selection = input('Which one would you would like to rent?')
    for movie in inventory:
        if selection in inventory:
            print(selection)


if __name__ == '__main__':
    main()
