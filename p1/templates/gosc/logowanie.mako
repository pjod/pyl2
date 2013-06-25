<%inherit file="/layout.mako"/>

${h.form('uwierzyt', method='post')}

    <fieldset>
    <legend>logowanie</legend>
        <div><label for="loginField">Login: </label>
            ${h.text("login")}</div>

        <div><label for="passwordField">Hasło: </label>
            ${h.password("password")}</div>
    </fieldset>

<div>${h.submit("uwierzyt", "Zaloguj")}</div>
</form>

${h.form('uwierzyt_admin', method='post')}

    <fieldset>
    <legend>logowanie admina</legend>
        <div><label for="loginField">Login: </label>
            ${h.text("login_admin")}</div>

        <div><label for="passwordField">Hasło: </label>
            ${h.password("password_admin")}</div>
    </fieldset>

<div>${h.submit("uwierzyt_admin", "Zaloguj admina")}</div>
</form>