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
    if cursor.rowcount == 1:
        cursor.execute("COMMIT")
        return True
    else:
        return False


def list(cursor):
    cursor.execute(
        "SELECT id, login, name, surname FROM users ORDER BY id"
        )
    return cursor.fetchall() if cursor.rowcount else None


def delete(cursor, id):
    try:
        cursor.execute(
            "DELETE FROM users WHERE id = %s", (id, )
            )
    except:
        print((cursor.query))
        raise
    if cursor.rowcount == 1:
        cursor.execute("COMMIT")
        return True
    else:
        return False


def get(cursor, id):
    cursor.execute(
        "SELECT login, name, surname FROM users WHERE id=%s", (id, )
        )
    return cursor.fetchone() if cursor.rowcount else None


def edit(cursor, login, password, name, surname, id_):
    try:
        cursor.execute(
            "UPDATE users SET login=%s, password=%s, name=%s, surname=%s WHERE \
            id=%s", (login, hash_pass(login, password), name, surname, id_,)
            )
        return True if cursor.rowcount == 1 else False