<%inherit file="/layout.mako"/>

${h.secure_form(url(controller="gosc", action="logowanie"), method ="POST")}
<button>Logowanie</button>
</form>
