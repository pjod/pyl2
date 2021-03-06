# -*- coding: utf-8 -*-
import hashlib
import psycopg2


class LoginDuplicate(Exception):
    pass


class Duplicate(Exception):
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


def add(cursor, login, password, name, surname):
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
    return cursor.rowcount == 1


def list_(cursor):
    cursor.execute(
        "SELECT id, login, name, surname FROM users ORDER BY id"
    )
    return cursor.fetchall()


def delete(cursor, id_):
    try:
        cursor.execute(
            "DELETE FROM users WHERE id = %s", (id_, )
        )
    except:
        print((cursor.query))
        raise
    return cursor.rowcount == 1


def get(cursor, id_):
    cursor.execute(
        "SELECT id, login, name, surname FROM users WHERE id=%s", (id_, )
    )
    return cursor.fetchone()


def edit(cursor, login, password, name, surname, id_):
    cursor.execute(
        "UPDATE users SET login=%s, password=%s, name=%s, surname=%s WHERE \
        id=%s", (login, hash_pass(login, password), name, surname, id_,)
        )
    return cursor.rowcount == 1


def add_file(cursor, user_id, filename):
#    try:
    cursor.execute(
        "INSERT INTO files (user_id, filename) VALUES (%s, %s) \
        RETURNING id", (user_id, filename,)
        )
#    except psycopg2.Error as e:
#        if "duplicate key" in e.pgerror:
#            raise Duplicate(e.pgerror)
#    print "  "
#    print cursor.fetchone().get('id')
    return cursor.fetchone().get('id')


def list_files(cursor, user_id):
    cursor.execute(
        "SELECT id, filename FROM files WHERE user_id=%s", (user_id,)
        )
    return cursor.fetchall()