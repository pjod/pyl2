# -*- coding: utf-8 -*-
${h.form(url(controller="admin", action="list_users"), method ="POST")}
<button>Zobacz/zarządzaj userami</button>
</form>

${h.secure_form(url(controller="admin", action="add_user_form"), method ="POST")}
<button>Dodaj usera</button>
</form>

${h.form(url(controller="uzytkownik", action="logout"), method ="POST")}
<button>Wyloguj się</button>
</form>
