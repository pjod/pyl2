# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<div><label for="del_loginField">Podaj login usera: </label>${h.text("del_login")}</div>
<button>Usuń usera!</button>
</fieldset>
</form>
<p>
<div id="menu"><%include file="/admin/menu.mako"/></div>