from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from p1.model.form import Dodaj_Usera
from pylons.decorators import validate
from psycopg2.extras import RealDictCursor
from p1.lib.base import BaseController, render
from pylons import app_globals as g
from p1.model.auth import dodaj
import psycopg2
import formencode


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
        except psycopg2.Error as e:
            if "\"users_login_key\"" in e.pgerror:
                print("duplikat!")
                from random import getrandbits
                kluczyk = getrandbits(20)
                session["duplikaty_kont_%s" % kluczyk] = request.POST
                redirect(url(action="form"))
            else:
                raise e
        finally:
            cursor.close()
            conn.close()
        if dodany:
            return "ok"
        else:
            return "duuuuupa:>"

#from random import getrandbits
#redirect(url(action="form", kluczyk=kluczyk))
    def form(self)
        if request.GET.get("kluczyk") and session.has_key(
            "duplikaty_kont_%s" %request.GET["kluczyk"]):
                formencode.htmlfill.render(szablon.mako, session["duplikaty_kont_%s...)
del session["duplikaty_kont_%s....]