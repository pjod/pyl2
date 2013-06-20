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

    def uwierzyt(self):
#        c.login = request.POST['login']
#        c.password = request.POST['password']
        return "dupa"