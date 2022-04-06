from swagger_server.logic import accounts
import json


def add_product(id_market, product, price):
    users = accounts.read_from_file()
    shops = read_from_file_shop()
    if accounts.auth and users[accounts.user]['status'] == 1:
        if id_market in users[accounts.user]['shops']:
            shops[str(id_market)]['goods'][product] = price
            write_to_file_shop(shops)
            return 0
        else:
            return 1
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return 2


def add_shop(shop):
    users = accounts.read_from_file()
    shops = read_from_file_shop()
    if accounts.auth and users[accounts.user]['status'] == 1:
        ids = len(shops) + 1
        users[accounts.user]["shops"].append(ids)
        accounts.write_to_file(users)
        print(shop)
        shops[ids] = {"area": shop.area,
                      "name": shop.name,
                      "owner": accounts.user,
                      "goods": shop.goods,
                      "orders": {}}
        write_to_file_shop(shops)
        return True
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return False


def get_shop_history():
    users = accounts.read_from_file()
    shops = read_from_file_shop()
    result = {}
    if accounts.auth and users[accounts.user]['status'] == 1:
        for id in users[accounts.user]["shops"]:
            result[str(id)] = shops[str(id)]
        return True, result
    else:
        accounts.auth = False
        users[accounts.user]['status'] = 0
        accounts.write_to_file(users)
        accounts.user = ''
        return False, {}


def write_to_file_shop(content):
    with open("C:\\Users\\Dimon\\PycharmProjects\\python-flask-server\\swagger_server\\logic\\shops.json", "w") as shops:
        shops.write(json.dumps(content, indent=4))


def read_from_file_shop():
    with open("C:\\Users\\Dimon\\PycharmProjects\\python-flask-server\\swagger_server\\logic\\shops.json", "r") as shops:
        return json.loads(shops.read())
