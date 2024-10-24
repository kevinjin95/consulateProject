from flask import render_template, redirect, url_for, flash, render_template
from consulate.user import createUser, checkUserConnexion, getUserdata
from consulate import app
from consulate.formConnexion import ConnexionForm
from consulate.formCreation import RegisterForm
from consulate.formProfil import ProfilForm
from flask_login import login_user
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('countryPresentation.html')

@app.route("/creationCompte",  methods=['GET', 'POST'])
def creationCompte_page():
    form = RegisterForm()
    if form.validate_on_submit():
        createUser(form)
        return redirect(url_for('profil_page'))
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f"there was errors when creating an user: {errMsg}", category='danger')
    return render_template('creationCompte.html', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    form = ConnexionForm()
    if form.validate_on_submit():
        if checkUserConnexion(form):
            # form2 = ProfilForm()
            login_user(form.emailAddress.data)
            flash(f"you are logged in as : { form.emailAddress.data }", category='success')
            # userInfo = getUserdata(form.emailAddress.data)
            print('connexion ok for: ', form.emailAddress.data)
            # print(userInfo)
            return redirect(url_for('profil_page'))
        else:
            flash("Username and password are not match, please try again!", category='danger')
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f'there was errors when creating an user: {errMsg}', category='danger')
    return render_template('connexion.html', form=form)

@app.route("/demandeVisa")
def demandeVisa_page():
    return render_template('demandeVisa.html')

@app.route("/profil",methods=['GET', 'POST'])
def profil_page():
    form = ProfilForm()
    # userInfo = getUserdata(form.emailAddress.data)
    return render_template('profil.html', form=form)
