import hashlib


def auth(login, password):
#    for user in USERS:
#        if login == user and \
#        hashlib.sha224(SOL_DO_HASEL + password).hexdigest() == \
#        USERS.get(user).get('haslo'):
#            return True
#    return False
    if USERS.get(login) and \
    hashlib.sha224(SOL_DO_HASEL + password).hexdigest() == \
    USERS[login]['haslo']:
        return True
    else:
        return False

SOL_DO_HASEL = "123sdf45"

USERS = {
    "john": {"id": 1, "haslo": hashlib.sha224(SOL_DO_HASEL + "dupa.8")
    .hexdigest(), "imie": "Jan", "nazwisko": "Kowalski"},
    "dupa": {"id": 2, "haslo": hashlib.sha224(SOL_DO_HASEL + "dupa123")
    .hexdigest(), "imie": "Genowefa", "nazwisko": "Tusk"}
    }
