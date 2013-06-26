<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

% if c.duplicate:
    <div><b> DUUUUUPa konto o podanym loginie już istnieje,
    popraw się albo napraw;></b></div>
% endif
<p>
${h.form(url(controller="admin", action="add_user"), method ="POST")}
<fieldset>
    <legend>Dodaj usera</legend>
<div><label for="loginField">Login: </label>${h.text("login")}</div>
<div><label for="passwordField">Hasło: </label>${h.password("password")}</div>
<div><label for="password_cField">Hasło ponownie: </label>
${h.password("password_c",)}</div>
<div><label for="nameField">Imię: </label>${h.text("name")}</div>
<div><label for="surnameField">Nazwisko: </label>${h.text("surname")}</div>
</fieldset>
<div>${h.submit("dodaj_usera", "Dodaj_usera")}</div>
</form>
<p>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
