from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from p1.model.form import Dodaj_Usera
from pylons.decorators import validate
from psycopg2.extras import RealDictCursor
from p1.lib.base import BaseController, render
from pylons import app_globals as g
from p1.model.auth import dodaj
import psycopg2

class AdminController(BaseController):

    def welcome(self):
        if session.get('admin'):
            c.nazwisko = session['admin']['nazwisko']
            return render('/admin/welcome.mako')
        else:
            return redirect(url(controller='gosc', action="logowanie"))

#    @validate(schema=Dodaj_Usera(), form="dodaj_usera")
    def dodaj_usera(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            dodany = dodaj(
                cursor, request.POST['login'], request.POST['password'],
                request.POST['name'], request.POST['surname']
                    )
            cursor.execute("commit")
        finally:
            cursor.close()
            conn.close()
        if dodany == 1:
            return "ok"
        else:
            return "duuuuupa:>"