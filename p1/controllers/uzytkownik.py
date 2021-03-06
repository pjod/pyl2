# -*- coding: utf-8 -*-
from pylons import session, tmpl_context as c, url
from pylons.controllers.util import redirect
from p1.lib.base import BaseController, render


class UzytkownikController(BaseController):

    def welcome(self):
        if session.get('user'):
            c.nazwisko = session['user']['surname']
            return render('/uzytkownik/welcome.mako')
        else:
            return redirect(url(controller='gosc', action="logowanie"))

    def logout(self):
        session.clear()
        session.save()
        return redirect(url(controller='gosc', action="welcome"))