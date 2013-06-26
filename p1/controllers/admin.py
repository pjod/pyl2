from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from p1.model.form import DodajUsera
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

    @validate(schema=DodajUsera(), form="dodaj_usera")
    def dodaj_usera(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            dodany = dodaj(
                cursor, request.POST['login'], request.POST['password'],
                request.POST['name'], request.POST['surname']
                    )
        except psycopg2.Error as e:
            if "\"users_login_key\"" in e.pgerror:
                from random import getrandbits
                kluczyk = getrandbits(20)
                session["duplikaty_kont_%s" % kluczyk] = request.POST
                session.save()
                redirect(
                    url(controller="admin", action="form", kluczyk=kluczyk)
                    )
            else:
                raise e
        finally:
            cursor.close()
            conn.close()
        if dodany:
            return "ok"
        else:
            return "duuuuupa:>"

    def form(self):
        if request.GET.get("kluczyk") and "duplikaty_kont_%s" \
        % request.GET["kluczyk"] in session:
            c.duplikat = True
            return formencode.htmlfill.render(
                render("/admin/panel.mako"), session["duplikaty_kont_%s"
                % request.GET["kluczyk"]])
            del session["duplikaty_kont_%s" % request.GET["kluczyk"]]
        c.duplikat = False
        return render("/admin/panel.mako")