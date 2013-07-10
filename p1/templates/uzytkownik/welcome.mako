<%inherit file="/layout.mako"/>

<h4>hejka ${c.nazwisko}!</h4>
<p>

% for i in c.records:
    <tr>
        <td>
        ${i["login"]}</td><td>${i["name"]}</td><td>${i["surname"]}
        </td>
    </tr>
% endfor





${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
