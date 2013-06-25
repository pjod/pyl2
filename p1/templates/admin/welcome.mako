<%inherit file="/layout.mako"/>

<h4>hejka ${c.nazwisko}!</h4>
<p>

${h.form(url(controller="admin", action="dodaj_usera"), method ="POST")}
<fieldset>
    <legend>Dodaj usera</legend>
<div><label for="loginField">Login: </label>${h.text("login")}</div>
<div><label for="passwordField">Hasło: </label>${h.password("password")}</div>
<div><label for="password_c">Hasło ponownie: </label>
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
