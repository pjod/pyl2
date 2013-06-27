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
        <td>${i["login"]}</td><td>${i["name"]}</td><td>${i["surname"]}</td>

        <td>${h.secure_form(url(controller="admin", action="edit_user_form"),
            method ="GET")}
            ${h.hidden("id", i["id"])}<button>Modyfikuj</button></form></td>

        <td>${h.secure_form(url(controller="admin", action="delete_user"),
            method ="POST")}
            ${h.hidden("id", i["id"])}<button>Usuń</button></form></td>
    </tr>
% endfor
</table>

<div id="menu"><%include file="/admin/menu.mako"/></div>