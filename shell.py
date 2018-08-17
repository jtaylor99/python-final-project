import core
import disk


def print_dictionary(rent_dictionary):
    for i, key in enumerate(rent_dictionary, start=1):
        print(
            i, '{}, stock:{}, price:{}, replacement cost:{}'.format(
                rent_dictionary[key]['name'], rent_dictionary[key]['stock'],
                rent_dictionary[key]['price'],
                rent_dictionary[key]['replacement cost']))


def define_customer_or_employee():
    person = input('Are you a customer or an employee?: ')
    if person == 'employee':
        return person
    elif person == 'customer':
        return person


def choices(rent_dictionary):
    print_dictionary(rent_dictionary)
    choice = input('Enter a number of the item you want to rent: ')
    if choice in rent_dictionary:
        return choice


def employee_options(rent_dictionary):
    while True:
        options = input(
            '1.check the stock\n2.check Transcation History and Total Revenue\n3.clock out: '
        )
        if options == '1':
            print_dictionary(rent_dictionary)
            continue
        elif options == '2':
            print(disk.read_history())
            print(f'Total Revenue:{disk.total_revenue()}')
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
                selection = choices(rent_dictionary)
                if rent_dictionary[selection]['stock'] == 0:
                    print('It\'s already rented')
                    continue
                else:
                    core.reduce_stock(rent_dictionary, selection)
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

                        disk.write_the_history(
                            core.create_history_string(name, 'check out',
                                                       selection, total))
                        file_string = core.create_file_string(rent_dictionary)
                        disk.write_file(file_string, 'inventory.txt')
                        break

            elif user_response == 'no':
                selection = print_dictionary(rent_dictionary)
                returning = input('What are you returning?: ')
                if returning in rent_dictionary:
                    print(
                        f'Thank you for returning {returning} and have a great day'
                    )
                    deposit = core.give_deposit(rent_dictionary, returning)
                    print(f'Here\'s your deposit:{deposit}')
                core.return_item(rent_dictionary, returning)
                disk.write_the_history(
                    core.create_history_string(name, 'check in', returning))

                file_string = core.create_file_string(rent_dictionary)
                disk.write_file(file_string, 'inventory.txt')
                exit()


if __name__ == '__main__':
    main()
