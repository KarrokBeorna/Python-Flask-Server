import json

auth = False
user = ''
password = ''


def create_user(body):
    users = read_from_file()
    if body.username not in users.keys():
        users[body.phone] = {"full_name": body.full_name,
                             "email": body.email,
                             "password": body.password,
                             "username": body.username,
                             "status": 0,
                             "orders": {},
                             "shops": []}
        write_to_file(users)
        return True
    return False


def user_login(usr, psw):
    global auth, user, password
    users = read_from_file()
    if usr in users.keys():
        if users[usr]['password'] == psw:
            user, password, auth = usr, psw, True
            users[usr]['status'] = 1
            write_to_file(users)
            return True
    return False


def user_logout():
    global auth
    users = read_from_file()
    if auth:
        users[user]['status'] = 0
        auth = False
        write_to_file(users)
        return True
    return False


def forced_user_logout(usr):
    global auth
    users = read_from_file()
    if auth and user == 'admin':
        users[usr]['status'] = 0
        write_to_file(users)
        return True
    return False


def write_to_file(content):
    with open("C:\\Users\\Dimon\\PycharmProjects\\python-flask-server\\swagger_server\\logic\\users.json", "w") as users:
        users.write(json.dumps(content, indent=4))


def read_from_file():
    with open("C:\\Users\\Dimon\\PycharmProjects\\python-flask-server\\swagger_server\\logic\\users.json", "r") as users:
        return json.loads(users.read())
