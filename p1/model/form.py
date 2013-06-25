import formencode


class Valid(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    login = formencode.validators.String(not_empty=True)
    password = formencode.validators.String(not_empty=True)


class Valid_Admin(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    login_admin = formencode.validators.String(not_empty=True)
    password_admin = formencode.validators.String(not_empty=True)