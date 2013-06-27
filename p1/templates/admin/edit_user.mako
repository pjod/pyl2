# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif
<p>
% if c.stat:
    <script type="text/javascript">alert("\
    % if c.stat == "success":
        Operacja się powiodła \
    % elif c.stat == "failure":
        Operacja nieudana \
    % endif
    ");</script>
% endif

${h.secure_form(url(controller="admin", action="edit_user"), method ="POST")}
<fieldset>
    <legend>Modyfikuj usera</legend>
<div><label for="loginField">Login: </label>${h.text("login")}</div>
<div><label for="passwordField">Hasło: </label>${h.password("password")}</div>
<div><label for="password_cField">Hasło ponownie: </label>
${h.password("password_c",)}</div>
<div><label for="nameField">Imię: </label>${h.text("name")}</div>
<div><label for="surnameField">Nazwisko: </label>${h.text("surname")}</div>
</fieldset>
<div>${h.submit("edit", "Zapisz")}</div>
</form>


<div id="menu"><%include file="/admin/menu.mako"/></div>