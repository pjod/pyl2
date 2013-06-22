#import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render


class UzytkownikController(BaseController):

    def welcome(self):
        if session.get('user'):
            import p1.model.users as users
            return render('/uzytkownik/welcome.mako',
            extra_vars={'juzer': users.USERS[session.get('user')]['nazwisko']})
        else:
            return redirect(url(controller='gosc', action="logowanie"))

    def logout(self):
        session.clear()
        session.save()
        return redirect(url(controller='gosc', action="welcome"))