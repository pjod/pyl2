# -*- coding: utf-8 -*-
import hashlib
import psycopg2


class LoginDuplicate(Exception):
    pass


def auth(cursor, login, password):
    cursor.execute(
        "SELECT id, login, password, imie, nazwisko FROM users \
        WHERE login=%s and password=%s", (login, hash_pass(password))
       )
    return cursor.fetchone() if cursor.rowcount else None


def hash_pass(password):
    SOL_DO_HASEL = "123sdf45"
    return hashlib.sha224(SOL_DO_HASEL + password).hexdigest()


def add(cursor, login, password, name, surname):
    try:
        cursor.execute(
        "INSERT INTO users (login, password, imie, nazwisko) \
        VALUES (%s, %s, %s, %s)", (login, hash_pass(password), name, surname)
        )
    except psycopg2.Error as e:
        if "\"users_login_key\"" in e.pgerror:
            raise LoginDuplicate(e)
            raise LoginDuplicate(e.pgerror)
    if cursor.rowcount == 1:
        cursor.execute("COMMIT")
        return True
    else:
        return False

#def view(cursor):
#    cursor.execute(
#        "SELECT *
#        )