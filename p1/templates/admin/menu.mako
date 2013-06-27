<%inherit file="/layout.mako"/>

${h.form(url(controller="admin", action="list_users"), method ="POST")}
<button>Zobacz userów</button>
</form>

${h.secure_form(url(controller="admin", action="delete_user_form"), method ="POST")}
<button>Usuń usera</button>
</form>

${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>

${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>