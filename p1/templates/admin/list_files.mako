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
        <img src="${url(config['app_conf']['dir_root'] +str(i['id']))}"
        name="${i['filename']}">
        </td>

    </tr>
% endfor
</table>

<div id="menu"><%include file="/admin/menu.mako"/></div>