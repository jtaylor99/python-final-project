import core
import disk

fake_dict = {
    '1': {
        'name': 'Die Hard',
        'stock': 10,
        'price': 5,
        'replacement cost': 10,
    }
}


def test_create_rent_dictionary():

    rent_info = '1, Die Hard, 10, 5, 10'.split('\n')
    result = core.create_rent_dictionary(rent_info)
    assert result == {
        '1': {
            'name': 'Die Hard',
            'stock': 10,
            'price': 5,
            'replacement cost': 10,
        }
    }


def test_rental_rates():
    result = core.rental_rates(fake_dict, '1')
    assert result == 6.35


def test_give_deposit():
    result = core.give_deposit(fake_dict, '1')

    assert result == 1.0


def test_create_file_string():
    result = core.create_file_string(fake_dict)
    assert result == ' key, name, stock, price, replacement cost\n1,Die Hard, 10, 5, 10'


def test_reduce_stock():
    result = core.reduce_stock(fake_dict, '1')
    assert result == 9


def test_return_item():
    result = core.return_item(fake_dict, '1')
    assert result == 10
