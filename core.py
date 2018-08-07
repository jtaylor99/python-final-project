def create_rent_dictionary():
    rent_dictionary = {
        'Die Hard': {
            'In stock': 10,
            'price': 5,
            'replacement cost': 10
        },
        'Dead Pool': {
            'In stock': 8,
            'price': 4,
            'replacement cost': 13
        },
        'Iron Man': {
            'In stock': 5,
            'price': 2,
            'replacement cost ': 4
        },
        'Black Panther': {
            'In stock': 1,
            'price': 13,
            'replacement cost': 26
        }
    }

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
    file_string = 'name, stock, price, replacement_cost'
    for key, value in rent_dictionary.items():
        name = key
        stock = value['In stock']
        price = value['price']
        replacement_cost = value['replacement cost']
    file_string += f'\n{name} {stock} {price} {replacement_cost}'
    return file_string
