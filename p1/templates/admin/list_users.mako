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

<div id="menu"><%include file="/admin/menu.mako"/></div>