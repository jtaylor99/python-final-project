def create_rent_dictionary(rent_info):
    rent_dictionary = {}
    for line in rent_info:
        item = line.split(',')
        key = item[0].strip()
        value = {
            'stock': int(item[1]),
            'price': int(item[2]),
            'replacement cost': int(item[3]),
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
        name = key
        stock = value['stock']
        price = value['price']
        replacement_cost = value['replacement cost']
        file_string = f'\n{name}, {stock}, {price}, {replacement_cost}'
    return file_string


def stock(item):
    stock -= 1
    if stock == 0:
        del item
