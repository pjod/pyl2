#import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render

#log = logging.getLogger(__name__)

class GoscController(BaseController):

#    def welcome(self):

#    def logowanie(self):
#        c.login = request.POST['login']
#        c.password = request.POST['password']

#    def uwierzyt(self):

