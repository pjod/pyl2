# -*- coding: utf-8 -*-
#import logging
import p1.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render

#log = logging.getLogger(__name__)

class GoscController(BaseController):

    def welcome(self):
        return render("gosc/welcome.mako")

    def logowanie(self):
        return render("gosc/logowanie.mako")

    def __before__(self, action, **params):
        user = session.get('user')
        if user:
            request.environ['REMOTE_USER'] = user

    def uwierzyt(self):
        if request.params['password'] == request.params['password'] and \
        request.params['login'] == request.params['login']:
            session['user'] = request.params['login']
            session.save()
            return redirect(url(controller='uzytkownik', action="welcome"))
        else:
            return "złe hasło lub login"
