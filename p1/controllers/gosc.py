# -*- coding: utf-8 -*-
#import logging
import p1.lib.helpers as h
import hashlib

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
from pylons import app_globals as g
from p1.lib.base import BaseController, render
from p1.model.form import Valid
from psycopg2.extras import RealDictCursor


class GoscController(BaseController):

    def __before__(self):
        self.conn = g.dbpool.connection()
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def __after__(self):
        self.cursor.close()
        self.conn.close()

    def welcome(self):
        return render("gosc/welcome.mako")

    def logowanie(self):
        return render("gosc/logowanie.mako")

    @validate(schema=Valid(), form="logowanie")
    def uwierzyt(self):
        if auth(
            self.cursor, request.POST['login'], request.POST['password']):
            session['user'] = request.POST['login']
            session.save()
            return redirect(url(controller='uzytkownik', action="welcome")
            )
        else:
            return "złe hasło lub login"


def auth(cursor, login, password):
    cursor.execute(
        "SELECT id FROM users WHERE login=%s and password=%s",
        (login, hash_pass(password))
        )
    row = cursor.fetchone()
    if row:
        cursor.execute(
            "SELECT * FROM users WHERE id=%s",
            (row['id'])
            )
        session['rekord'] = cursor.fetchone()
        c.nazwisko = session['rekord']['nazwisko']
        session.save()
        return True
    else:
        return False


def hash_pass(password):
    SOL_DO_HASEL = "123sdf45"
    return hashlib.sha224(SOL_DO_HASEL + password).hexdigest()