# -*- coding: utf-8 -*-
#import logging
import p1.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render


class GoscController(BaseController):

    def welcome(self):
        return render("gosc/welcome.mako")

    def logowanie(self):
        return render("gosc/logowanie.mako")

    def uwierzyt(self):
        if request.POST['password'] == request.POST['password'] and \
        request.POST['login'] == request.POST['login']:
            session['user'] = request.POST['login']
            session.save()
            return redirect(url(controller='uzytkownik', action="welcome"))
        else:
            return "złe hasło lub login"
