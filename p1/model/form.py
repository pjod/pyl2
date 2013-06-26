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


class Dodaj_Usera(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    login = formencode.All(
        formencode.validators.MinLength(4, not_empty=True),
        formencode.validators.MaxLength(8)
        )
    password = formencode.All(
        formencode.validators.MinLenght(8, not empty=True),
        formencode.validators.MaxLength(22)
        )
    password_c = formencode.validators.String()
    chained_validatore = [formencode.validators.FieldsMatch('password',
        'password_c')]
    name = formencode.validators.String(not_empty=True)
    surname = formencode.validators.String(not_empty=True)