# -*- coding: utf-8 -*-
<%inherit file="/layout.mako"/>

% if c.surname:
    <h4>jesteś zalogowany jako: ${c.surname}</h4>
% endif

<div>User usunięty!</div>

</fieldset>
</form>
<p>
<div id="menu"><%include file="/admin/menu.mako"/></div>