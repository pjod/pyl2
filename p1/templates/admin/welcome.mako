<%inherit file="/layout.mako"/>

<h4>hejka ${c.nazwisko}!</h4>
<p>
${h.form(url(controller="admin", action="form"), method ="POST")}
<button>Dodaj usera</button>
</form>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
