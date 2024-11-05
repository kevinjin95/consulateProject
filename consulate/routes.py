from flask import render_template, redirect, url_for, flash
from consulate.models import Users
from consulate import app
from consulate.formConnexion import ConnexionForm
from consulate.formCreation import RegisterForm
from consulate.formProfil import ProfilForm
# from flask_login import login_user, login_required, logout_user, 
from consulate import db
from flask import Flask
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('countryPresentation.html')

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/accountCreation",  methods=['GET', 'POST'])
def accountCreation_page():
    form = RegisterForm()
    if form.validate_on_submit():
        userToCreate = Users(
            userName=form.userName,
            emailAddress=form.emailAddress,
            passwordHash=form.password1,
            )
        db.session.add(userToCreate)
        db.session.commit()
        return redirect(url_for('connexion_page'))
    if form.errors != {}:
        for errMsg in form.errors.values():
            print(f"there was errors when creating an user: {errMsg}", category='danger')
            flash(f"there was errors when creating an user: {errMsg}", category='danger')
    return render_template('accountCreation.html', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    form = ConnexionForm()
    if form.validate_on_submit():
        userToCreate = Users(
            userName=form.userName,
            emailAddress=form.emailAddress,
            password1=form.password,
            )
        db.session.add(userToCreate)
    #     if checkUserConnexion(form):
    #         login_user(getUserId(form.userName.data))
    #         login_user(form.emailAddress.data)
    #         flash(f"you are logged in as : { form.emailAddress.data }", category='success')
    #         userInfo = getUserdata(form.emailAddress.data)
    #         print('connexion ok for: ', form.emailAddress.data)
    #         print(userInfo)
    #         return redirect(url_for('profil_page'))
    #     else:
    #         flash("Username and password are not match, please try again!", category='danger')
    # if form.errors != {}:
    #     for errMsg in form.errors.values():
    #         flash(f'there was errors when creating an user: {errMsg}', category='danger')
    return render_template('connexion.html', form=form)

@app.route("/demandeVisa")
# @login_required
def demandeVisa_page():
    return render_template('demandeVisa.html')

@app.route("/profil",methods=['GET', 'POST'])
# @login_required
def profil_page():
    form = ProfilForm()
#     # userInfo = getUserdata(form.emailAddress.data)
    return render_template('profil.html', form=form)

@app.route('/home', methods=['GET', 'POST'])
# @login_required
def logout():
#     logout_user()
    return redirect(url_for('countryPresentation'))

