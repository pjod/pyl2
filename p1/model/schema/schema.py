# -*- coding: utf-8 -*-
import formencode


class Valid(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    login = formencode.validators.String(not_empty=True)
    password = formencode.validators.String(not_empty=True)


class ValidAdmin(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    login_admin = formencode.validators.String(not_empty=True)
    password_admin = formencode.validators.String(not_empty=True)


class User(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    login = formencode.validators.String(min=4, max=8)
    name = formencode.validators.String(not_empty=True)
    surname = formencode.validators.String(not_empty=True)


class EditUser(User):
    pass


class AddUser(User):
#    pass
    password = formencode.validators.String(min=8, max=16)
    password_c = formencode.validators.String()
    chained_validators = [formencode.validators.FieldsMatch('password',
        'password_c')]