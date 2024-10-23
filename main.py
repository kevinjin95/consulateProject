from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages
from formConnexion import ConnexionForm
from formCreation import RegisterForm
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = '44d9de2b82a1deb9057de798'
bcrypt = Bcrypt(app)
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('presentationPays.html')

@app.route("/creationCompte",  methods=['GET', 'POST'])
def creationCompte_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # userToCreate=[form.emailAddress.data, form.password.data]
        # print(userToCreate)
        return redirect(url_for('profil_page'))
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f"there was errors when creating an user: {errMsg}", category='danger')
    return render_template('creationCompte.html', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    form = ConnexionForm()
    if form.validate_on_submit():
        userToCreate=[form.emailAddress.data, form.password.data]
        print(userToCreate)
        return redirect(url_for('profil_page'))
    if form.errors != {}:
        for errMsg in form.errors.values():
            # flash(f'there was errors when creating an user: {errMsg}', category='danger')
            print(f'there was errors when creating an user: {errMsg}', category='danger')

    return render_template('connexion.html', form=form)

@app.route("/demandeVisa")
def demandeVisa_page():
    return render_template('demandeVisa.html')

@app.route("/profil")
def profil_page():
    return render_template('profil.html')
