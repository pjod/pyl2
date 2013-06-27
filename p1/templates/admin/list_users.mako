<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<table>
<tr>
<th>lp</th>
<th>id</th>
<th>login</th>
<th>imię</th>
<th>nazwisko</th>
</tr>
<%
    j = 1
%>

% for i in c.records:
    <tr>

            <td>${j}</td>
<%
    j += 1
%>
        <td>${i["id"]}</td><td>${i["login"]}</td>
        <td>${i["imie"]}</td><td>${i["nazwisko"]}</td>
    </tr>
% endfor
</table>

${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
