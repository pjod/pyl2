# -*- coding: utf-8 -*-
import hashlib
import psycopg2


class LoginDuplicate(Exception):
    pass


def auth(cursor, login, password):
    cursor.execute(
        "SELECT id, login, password, name, surname FROM users \
        WHERE login=%s and password=%s", (login, hash_pass(login, password))
    )
    return cursor.fetchone() if cursor.rowcount else None


def hash_pass(login, password):
    sol = "123sdf45"
    return hashlib.sha224(login + sol + password).hexdigest()


def add(cursor, login, password, password_c, name, surname):
    try:
        cursor.execute(
            "INSERT INTO users (login, password, name, surname) \
            VALUES (%s, %s, %s, %s)",
            (login, hash_pass(login, password), name, surname)
        )
    except psycopg2.Error as e:
        if "\"users_login_key\"" in e.pgerror:
            raise LoginDuplicate(e)
            raise LoginDuplicate(e.pgerror)
    return True if cursor.rowcount == 1 else False


def list(cursor):
    cursor.execute(
        "SELECT id, login, name, surname FROM users ORDER BY id"
    )
    return cursor.fetchall() if cursor.rowcount else None


def delete(cursor, id_):
    try:
        cursor.execute(
            "DELETE FROM users WHERE id = %s", (id_, )
        )
    except:
        print((cursor.query))
        raise
    return True if cursor.rowcount == 1 else False


def get(cursor, id_):
    cursor.execute(
        "SELECT login, name, surname FROM users WHERE id=%s", (id_, )
    )
    return cursor.fetchone() if cursor.rowcount else None


def edit(cursor, login, password, name, surname, id_):
    cursor.execute(
        "UPDATE users SET login=%s, password=%s, name=%s, surname=%s WHERE \
        id=%s", (login, hash_pass(login, password), name, surname, id_,)
        )
    return True if cursor.rowcount == 1 else False