def create_rent_dictionary(rent_info):
    rent_dictionary = {}
    for line in rent_info:
        item = line.split(',')
        key = item[0].strip()
        value = {
            'name': item[1].strip(),
            'stock': int(item[2].strip()),
            'price': int(item[3].strip()),
            'replacement cost': int(item[4].strip()),
        }
        rent_dictionary[key] = value

    return rent_dictionary


def rental_rates(rent_dictionary, key):
    '''(int,int) -> int
    Returns the rental rates 
    '''
    sales_tax = 0.07 + 1
    price = rent_dictionary[key]['price'] * sales_tax
    replacement_cost = rent_dictionary[key]['replacement cost'] * 0.10
    rental_rates = price + replacement_cost
    return round(rental_rates, 2)


def give_deposit(rent_dictionary, key):
    deposit = rent_dictionary[key]['replacement cost'] / 10
    return deposit


def create_file_string(rent_dictionary):
    file_string = ' key, name, stock, price, replacement cost'
    for key, value in rent_dictionary.items():
        name = value['name']
        stock = value['stock']
        price = value['price']
        replacement_cost = value['replacement cost']
        file_string += f'\n{key},{name}, {stock}, {price}, {replacement_cost}'
    return file_string


def reduce_stock(rent_dictionary, key):
    rent_dictionary[key]['stock'] -= 1
    return rent_dictionary[key]['stock']


def return_item(rent_dictionary, key):
    rent_dictionary[key]['stock'] += 1
    return rent_dictionary[key]['stock']


def create_history_string(name, type, selection, total):
    history_string = f'{name.upper()}, {type}, {selection}, {total}\n'
    return history_string
