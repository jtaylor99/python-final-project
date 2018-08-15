import core
import disk


def print_dictionary(rent_dictionary):
    for i, key in enumerate(rent_dictionary):
        print(
            i, '{}, stock:{}, price:{}, replacement cost:{}'.format(
                key, rent_dictionary[key]['stock'],
                rent_dictionary[key]['price'],
                rent_dictionary[key]['replacement cost']))


def define_customer_or_employee():
    person = input('Are you a customer or an employee?: ')
    if person == 'employee':
        return person
    elif person == 'customer':
        return person


def employee_options(rent_dictionary):
    while True:
        options = input(
            '1.check the stock\n2.check Transcation History\n3.clock out: ')
        if options == '1':
            print_dictionary(rent_dictionary)
            continue
        elif options == '2':
            print(disk.read_history())
            continue
        elif options == '3':
            exit()


def main():
    rent_info = disk.open_file('inventory.txt')
    rent_dictionary = core.create_rent_dictionary(rent_info)

    print('Welcome to the Rental store!')
    name = input('What\'s your name?: ')
    print(f'Hello {name.upper()}')
    choice = define_customer_or_employee()
    if choice == 'employee':
        employee_options(rent_dictionary)
    elif choice == 'customer':
        while True:
            user_response = input('Would you like to rent anything? ')
            # this is a yes or no question
            if user_response == 'yes':
                print('These is what we have in stock')
                print_dictionary(rent_dictionary)
                break
            elif user_response == 'no':
                print_dictionary(rent_dictionary)
                returning = input('What are you returning?: ')
                if returning in rent_dictionary:
                    print(
                        f'Thank you for returning {returning} and have a great day'
                    )
                    deposit = core.give_deposit(rent_dictionary, returning)
                    print(f'Here\'s your deposit:{deposit}')
                core.return_item(rent_dictionary, returning)

                file_string = core.create_file_string(rent_dictionary)
                disk.write_file(file_string, 'inventory.txt')
                exit()

        while True:
            selection = input('Which one would you would like to rent?: ')
            if selection in rent_dictionary:
                if rent_dictionary[selection]['stock'] == 0:
                    print('It\'s already rented')
                    continue
            else:
                print(f'you have selected {selection}')
                break
        if selection not in rent_dictionary:
            print('please choose a valid option!')
        total = core.rental_rates(rent_dictionary, selection)
        days = input('How many days do you want to rent this?: ')
        if days.isdigit():
            total = total * int(days)
        print('----------------')
        print('Here\'s your receipt')
        print('----------------')
        print(f'total: {total:.2f}')
        print('Thank for your service')
        print('----------------')
        core.reduce_stock(rent_dictionary, selection)
        disk.write_the_history(name, selection, 'history.txt')
        file_string = core.create_file_string(rent_dictionary)
        disk.write_file(file_string, 'inventory.txt')


if __name__ == '__main__':
    main()
