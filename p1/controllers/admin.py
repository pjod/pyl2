# -*- coding: utf-8 -*-
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from p1.model.schema.schema import AddUser
from pylons.decorators import validate
from psycopg2.extras import RealDictCursor
from p1.lib.base import BaseController, render
from pylons import app_globals as g
import p1.model as model
#import psycopg2
import formencode
from pylons.decorators.secure import authenticate_form


class AdminController(BaseController):

    def welcome(self):
        if session.get('admin'):
            c.surname = session['admin']['nazwisko']
            return render('/admin/welcome.mako')
        else:
            return redirect(url(controller='gosc', action="logowanie"))

    @validate(schema=AddUser(), form="add_user_form")
    @authenticate_form
    def add_user(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        err = "unknown"
        added = False
        try:
            added = model.user.add(
                cursor, request.POST['login'], request.POST['password'],
                request.POST['password'], request.POST['name'],
                request.POST['surname']
                    )
        except model.user.LoginDuplicate:
            err = "duplikat"
        finally:
            cursor.close()
            conn.close()
        if added:
            return redirect(
                url(controller="admin", action="list_users", stat="success"))
        else:
            from random import getrandbits
            key = getrandbits(20)
            session["duplikaty_kont_%s" % key] = request.POST
            session.save()
            redirect(
                url(controller="admin", action="add_user_form",
                    key=key, err=err)
                )

    def add_user_form(self):
        c.surname = session['admin']['nazwisko']
        if request.GET.get("key") and "duplikaty_kont_%s" \
        % request.GET["key"] in session:
            c.duplicate = True
            return formencode.htmlfill.render(
                render("/admin/panel.mako"), session["duplikaty_kont_%s"
                % request.GET["key"]])
            del session["duplikaty_kont_%s" % request.GET["key"]]
        c.duplicate = False
        return render("/admin/panel.mako")

    def list_users(self):
        if "stat" in request.GET:
            c.stat = request.GET["stat"]
        else:
            c.stat = None
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
#        list_ = []
        try:
            list_ = model.user.list(cursor)
        finally:
            cursor.close()
            conn.close()
        c.surname = session['admin']['nazwisko']
        c.records = list_
        return render("admin/list_users.mako")

#    def delete_user_form(self):
#        c.surname = session['admin']['nazwisko']
#        return render("admin/delete_user.mako")

    def delete_user(self):
        conn = g.dbpool.connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        c.surname = session['admin']['nazwisko']
        try:
            success = model.user.delete(cursor, request.POST['id'])
        finally:
            cursor.close()
            conn.close()
        if success:
            redirect(
                url(controller="admin", action="list_users", stat="success"))
        else:
            redirect(
                url(controller="admin", action="list_users", stat="failure"))
#    def modify_user(self):