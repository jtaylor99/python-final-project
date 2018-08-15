def create_rent_dictionary(rent_info):
    rent_dictionary = {}
    for line in rent_info:
        item = line.split(',')
        key = item[0].strip()
        value = {
            'stock': int(item[1].strip()),
            'price': int(item[2].strip()),
            'replacement cost': int(item[3].strip()),
        }
        rent_dictionary[key] = value

    return rent_dictionary


def rental_rates(rent_dictionary, item_name):
    '''(int,int) -> int
    Returns the rental rates 
    '''
    sales_tax = 0.07 + 1
    price = rent_dictionary[item_name]['price'] * sales_tax
    replacement_cost = rent_dictionary[item_name]['replacement cost'] * 0.10
    rental_rates = price + replacement_cost
    return rental_rates


def create_file_string(rent_dictionary):
    file_string = 'name, stock, price, replacement cost'
    for key, value in rent_dictionary.items():
        stock = value['stock']
        price = value['price']
        replacement_cost = value['replacement cost']
        file_string += f'\n{key}, {stock}, {price}, {replacement_cost}'
    return file_string


def reduce_stock(rent_dictionary, item_name):
    rent_dictionary[item_name]['stock'] -= 1
    return rent_dictionary


def return_item(rent_dictionary, item_name):
    rent_dictionary[item_name]['stock'] += 1
    return rent_dictionary
