def create_rent_dictionary(rent_list):
    rent_dictionary = {}
    for rent_info in rent_list:
        items = rent_info.split(',')
        name = items[0].strip()
        stock = int(items[1])
        price = int(items[2])
        replacement_cost = int(items[3])
        rent_dictionary[name] = stock, price, replacement_cost
    return rent_dictionary


def create_file_string(rent_dictionary):
    ''' ({str: int} -> str)
    turns the user_dictionary
    '''
    for name, stock, price, replacement_cost in rent_dictionary.items():
        file_string = f'\n{name}, {stock}, {price}, {replacement_cost}'
    return file_string
