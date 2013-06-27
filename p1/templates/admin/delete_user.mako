# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<div>${c.delete}</div>

${h.secure_form(url(controller="admin", action="delete_user"), method ="POST")}
<fieldset>
    <legend>Usuń usera!</legend>
<div><label for="del_loginField">Podaj login usera: </label>${h.text("del_login")}</div>
</form>

${h.secure_form(url(controller="admin", action="delete_user"), method ="POST")}
<button>Usuń usera</button>
</form>
${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
