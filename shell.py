import core
import disk


def main():
    filename = 'inventory.txt'
    rent_info = disk.open_file()
    rent_dictionary = core.create_rent_dictionary()
    print('Welcome to the Rental store!')
    name = input('What\'s your name?:')
    print(f'Hello {name.upper()}')
    while True:
        user_response = input('Would you like to rent anything?')
        # this is a yes or no question
        if user_response == 'yes':
            print('These is what we have in stock')
            print(rent_dictionary)
            break
        elif user_response == 'no':
            returning = input('What are you returning?:')
            if returning in rent_dictionary:
                print(
                    f'Thank you for returning {returning} and have a great day'
                )
                exit()
            else:
                print('Please choose a valid option!')
    while True:
        selection = input('Which one would you would like to rent?')
        if selection in rent_dictionary:
            print(f'you have selected {selection}')
            break
        if selection not in rent_dictionary:
            print('please choose a valid option!')
    total = core.rental_rates(rent_dictionary, selection)
    days = input('How many days do you want to rent this?')
    if days.isdigit():
        total = total * int(days)
    print('----------------')
    print('Here\'s your receipt')
    print('----------------')
    print(f'total: {total:.2f}')
    print('Thank for your service')
    print('----------------')
    disk.write_the_history(name, selection)
    file_string = core.create_file_string(rent_dictionary)
    disk.write_file(file_string)


if __name__ == '__main__':
    main()
