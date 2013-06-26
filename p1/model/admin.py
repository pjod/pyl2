# -*- coding: utf-8 -*-
import hashlib


def auth(cursor, login, password):
    cursor.execute(
        "SELECT id, login, password, imie, nazwisko FROM admins \
        WHERE login=%s and password=%s",
        (login, hash_pass(password))
       )
    return cursor.fetchone() if cursor.rowcount else None


def hash_pass(password):
    SOL_DO_HASEL = "123sdf45"
    return hashlib.sha224(SOL_DO_HASEL + password).hexdigest()