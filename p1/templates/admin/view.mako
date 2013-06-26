<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<table>
<tr>
<th>id</th>
<th>login</th>
<th>imię</th>
<th>nazwisko</th>
% for i in c.records:
    <tr>
    %for j in i:
            <td> ${ j }</td>
    % endfor
    </tr>

% endfor
</table>

${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>
${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
