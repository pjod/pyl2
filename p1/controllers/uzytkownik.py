#import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render

#log = logging.getLogger(__name__)

class UzytkownikController(BaseController):

    def welcome(self):
        if request.environ.get("REMOTE_USER"):
            return render('/uzytkownik/welcome.mako')
        else:
            return redirect(url(controller='gosc', action="logowanie"))

    def logout(self):
        session['user'] = ""
        session.save()
        return redirect(url(controller='gosc', action="welcome"))