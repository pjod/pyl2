# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif
<p>
<h5> Obrazeczki usera o lognienie ${c.login}:</h5>

<table>

% for i in c.records:
    <tr>

        <td>
        ${h.hidden("id", i["id"])}
        <img src="${url(controller='admin', action='get_file')}"
        name="${i['filename']}"/>
        </td>

    </tr>
% endfor
</table>

<div id="menu"><%include file="/admin/menu.mako"/></div>