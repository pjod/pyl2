# -*- coding: utf-8 -*-
import p1.lib.helpers as h
import p1.model as model

from pylons import request, session, tmpl_context as c, url
from pylons.controllers.util import redirect
from pylons.decorators import validate
from pylons import app_globals as g
from p1.lib.base import BaseController, render
from p1.model.schema import schema as sch
from psycopg2.extras import RealDictCursor
from pylons.decorators.secure import authenticate_form


class GoscController(BaseController):

    def welcome(self):
        return render("gosc/welcome.mako")

    def logowanie(self):
        return render("gosc/logowanie.mako")

    @validate(schema=sch.Valid(), form="logowanie")
    @authenticate_form
    def uwierzyt(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            logged_in = model.user.auth(
                cursor, request.POST['login'], request.POST['password']
                )
        finally:
            cursor.close()
            conn.close()
        if logged_in:
            session['user'] = logged_in
            session.save()
            return redirect(url(controller='uzytkownik', action="welcome"))
        else:
            return "złe hasło lub login"

    @validate(schema=sch.ValidAdmin(), form="logowanie")
    @authenticate_form
    def uwierzyt_admin(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            logged_in = model.admin.auth(
                cursor, request.POST['login_admin'],
                request.POST['password_admin']
                )
        finally:
            cursor.close()
            conn.close()
        if logged_in:
            session['admin'] = logged_in
            session.save()
            return redirect(url(controller='admin', action="welcome"))
        else:
            return "złe hasło lub login"