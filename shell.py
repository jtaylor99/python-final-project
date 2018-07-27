import core
import disk


def main():
    filename = 'inventory.txt'
    rent_info = disk.open_file()
    rent_dictionary = core.create_rent_dictionary(rent_info)
    print('Welcome to the Rental store!')
    user_response = input('Would you like to rent anything?')
    # this is a yes or no question
    if user_response == 'yes':
        print('These is what we have in stock')
        print(rent_dictionary)
    elif user_response == 'no':
        print('Thank you have a great day!')
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
    days = input('how many days do you want to rent this?:')
    total = rental_rates(rent_dictionary, selection)
    print('----------------')
    print('Here\'s your receipt')
    print('----------------')
    print(f'total: {total:.2f}')
    print('----------------')
    file_string = core.create_file_string(rent_dictionary)
    disk.write_file(file_string)


if __name__ == '__main__':
    main()
