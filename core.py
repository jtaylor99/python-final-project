def create_rent_dictionary(rent_list):
    rent_dictionary = {}
    for rent_info in rent_list:
        item = rent_info.split(',')
        key = item[0].strip()
        value_1 = int(item[1].strip())
        value_2 = int(item[2].strip())
        value_3 = int(item[3].strip())
        rent_dictionary[key] = value_1, value_2, value_3
    return rent_dictionary


def create_file_string(rent_dictionary):
    file_string = 'name, stock, price, replacement_cost'
    for key, value in rent_dictionary.items():
        name, stock, price, replacement_cost = rent_dictionary.values()
        file_string = f'{name} ({stock}, {price)}, {int(replacement_cost)})'
    return file_string
