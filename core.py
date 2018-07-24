def rental_rates(name, in_stock, sales_tax, replacement_value):
    '''(int,int,int) -> int
    Returns the rental rates 
    '''
    'name' = name
    'in_stock' = in_stock
    sales_tax = 0.07
    replacement_value = replacement_value * 0.10
    rental_rates = sales_tax + replacement_value
    return rental_rates
