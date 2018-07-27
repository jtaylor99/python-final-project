def create_rent_dictionary(rent_list):
    rent_dictionary = {}
    for rent_info in rent_list:
        items = rent_info.split(',')
        name = items[0].split(',')
        stock = int(items[1])
        price = int(items[2])
        replacement_cost = int(items[3])
        rent_dictionary = name, stock, price, replacement_cost
    return rent_dictionary


def rental_rates(rent_dictionary, item_name):
    '''(int,int) -> int
    Returns the rental rates 
    '''
    sales_tax = 0.07 + 1
    price = rent_dictionary[item_name][1] * sales_tax
    replacement_cost = rent_dictionary[item_name][2] * 0.10
    rental_rates = price + replacement_cost
    return rental_rates


def create_file_string(rent_dictionary):
    ''' ({str: int} -> str)
    turns the user_dictionary
    '''
    file_string = 'name', stock, price, replacement_cost
    for name in rent_dictionary.items():
        file_string = f'{name} ({stock}, {int(price)}, {int(replacement_cost)})'
    return file_string
