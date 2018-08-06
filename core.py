def create_rent_dictionary(rent_list):
    rent_dictionary = {}
    for rent_info in rent_list:
        items = rent_info.split(',')
        key = items[0].strip()
        value_1 = int(items[1].strip())
        value_2 = int(items[2].strip())
        value_3 = int(items[3].strip())
        rent_dictionary[key] = value_1, value_2, value_3
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
    file_string = 'name, stock, price, replacement_cost'
    for key, value in rent_dictionary.items():
        name = value['name']
        stock = value['stock']
        price = value['price']
        replacement_cost = value['replacement_cost']
    file_string += f'{name}\n{stock}\n{price}\n{replacement_cost}\n'
    return file_string
