#import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from p1.lib.base import BaseController, render

#log = logging.getLogger(__name__)

class UzytkownikController(BaseController):

#    def welcome(self):

#    def logout(self):
