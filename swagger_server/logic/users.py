import datetime
from swagger_server.logic import accounts, vendors


def create_order(body):
    users = accounts.read_from_file()
    shops = vendors.read_from_file_shop()
    if accounts.auth and users[accounts.user]['status'] == 1:
        ids = len(users[accounts.user]["orders"]) + 1
        try:
            order_price = 0
            for product in body.goods:
                order_price += body.goods[product] * shops[str(body.shop)]['goods'][product]

            users[accounts.user]["orders"][ids] = {'shop': body.shop,
                                                   'name_shop': shops[str(body.shop)]['name'],
                                                   'goods': body.goods,
                                                   'area': body.area,
                                                   'order_date': str(datetime.datetime.now()),
                                                   'order_price': order_price,
                                                   'cost_of_delivery': 1000 * abs(body.area -
                                                                                  shops[str(body.shop)]['area'])}
        except Exception:
            return 2
        accounts.write_to_file(users)
        ids = len(shops[str(body.shop)]["orders"]) + 1
        shops[str(body.shop)]["orders"][ids] = {'order_date': str(datetime.datetime.now()),
                                                'area': body.area,
                                                'order_price': order_price,
                                                'goods': body.goods}
        vendors.write_to_file_shop(shops)
        return 0
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return 1


def get_order_history():
    users = accounts.read_from_file()
    if accounts.auth and users[accounts.user]['status'] == 1:
        return True, users[accounts.user]["orders"]
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return False, []


def get_shops():
    users = accounts.read_from_file()
    shops = vendors.read_from_file_shop()
    if accounts.auth and users[accounts.user]['status'] == 1:
        result = {}
        for id in shops:
            result[id] = {"area": shops[id]['area'], "name": shops[id]['name'], "goods": shops[id]['goods']}
        return True, result
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return False, {}
