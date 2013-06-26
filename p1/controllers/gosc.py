# -*- coding: utf-8 -*-
#import logging
import p1.lib.helpers as h

from pylons import request, session, tmpl_context as c, url
from pylons.controllers.util import redirect
from pylons.decorators import validate
from pylons import app_globals as g
from p1.lib.base import BaseController, render
from p1.model.form import Valid
from p1.model.firm import ValidAdmin
from p1.model.auth import auth, auth_admin
from psycopg2.extras import RealDictCursor


class GoscController(BaseController):

    def welcome(self):
        return render("gosc/welcome.mako")

    def logowanie(self):
        return render("gosc/logowanie.mako")

    @validate(schema=Valid(), form="logowanie")
    def uwierzyt(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            zalogowany = auth(
                cursor, request.POST['login'], request.POST['password']
                )
        finally:
            cursor.close()
            conn.close()
        if zalogowany:
            session['user'] = zalogowany
            session.save()
            return redirect(url(controller='uzytkownik', action="welcome"))
        else:
            return "złe hasło lub login"

    @validate(schema=ValidAdmin(), form="logowanie")
    def uwierzyt_admin(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            zalogowany = auth_admin(
                cursor, request.POST['login_admin'],
                request.POST['password_admin']
                )
        finally:
            cursor.close()
            conn.close()
        if zalogowany:
            session['admin'] = zalogowany
            session.save()
            return redirect(url(controller='admin', action="welcome"))
        else:
            return "złe hasło lub login"