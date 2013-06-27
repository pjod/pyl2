# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<table>
<tr>
<th>lp</th>
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
        <td>${i["login"]}</td><td>${i["imie"]}</td><td>${i["nazwisko"]}</td>

        <td>${h.secure_form(url(controller="admin", action="modify_user_form"),
            method ="POST")}
            ${h.hidden("id", i["id"])}<button>Modyfikuj</button></form></td>

        <td>${h.secure_form(url(controller="admin", action="delete_user"),
            method ="POST")}
            ${h.hidden("id", i["id"])}<button>Usuń</button></form></td>
    </tr>
% endfor
</table>

<div id="menu"><%include file="/admin/menu.mako"/></div>