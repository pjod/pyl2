<%inherit file="/layout.mako"/>

${h.form('uwierzyt', method='post')}

    <fieldset>
    <legend>logowanie</legend>
        <div><label for="loginField">Login: </label>
            ${h.text("login", id="loginField")}</div>

        <div><label for="passwordField">Hasło: </label>
            ${h.password("password", id="passwordField")}</div>
    </fieldset>

<div>${h.submit("uwierzyt", "Zaloguj")}</div>
