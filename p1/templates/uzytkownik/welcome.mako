<%inherit file="/layout.mako"/>

<h4>hejka ${juzer}!</h4>
<p>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
