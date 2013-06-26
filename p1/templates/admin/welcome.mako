<%inherit file="/layout.mako"/>

<h4>hejka ${c.surname}!</h4>
<p>
${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
