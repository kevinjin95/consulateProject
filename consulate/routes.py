from flask import render_template, redirect, url_for, flash
from consulate.models import User, Home, Person
from consulate import app, db, bcrypt
from consulate.formConnexion import ConnexionForm
from consulate.formCreation import RegisterForm
from consulate.formProfil import ProfilForm
from flask_login import login_user, login_required, logout_user
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('countryPresentation.html')

@app.route("/accountCreation",  methods=['GET', 'POST'])
def accountCreation_page():
    form = RegisterForm()
    if form.validate_on_submit():
        userToCreate = User(
            userName=form.userName.data,
            emailAddress=form.emailAddress.data,
            setPassword=form.password1.data
            )
        db.session.add(userToCreate)
        db.session.commit()
        return redirect(url_for('connexion_page'))
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f"there was errors when creating an user: {errMsg}", category='danger')
    return render_template('accountCreation.html', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    form = ConnexionForm()
    if form.validate_on_submit():
        attemptedUser = User.query.filter_by(userName=form.userName.data).first()
        print('from form: ', form.password.data)
        print('from db: ', attemptedUser.password)
        # attemptedUser.checkPassword = form.password.data
        # attemptedUser.checkPassword)
        if attemptedUser and bcrypt.check_password_hash(attemptedUser.password, form.password.data):
            login_user(attemptedUser)
            flash(f"you are logged in as: { attemptedUser.userName } !", category='success')
            return redirect(url_for('profil_page'))
        else:
            flash('the connection failed, please retry !', category='danger')
    return render_template('connexion.html', form=form)

@app.route("/demandeVisa")
@login_required
def demandeVisa_page():
    return render_template('demandeVisa.html')

@app.route("/profil",methods=['GET', 'POST'])
@login_required
def profil_page():
    form = ProfilForm()
    if form.validate_on_submit():
        userToCreate = User(
            userName=form.userName.data,
            emailAddress=form.emailAddress.data,
            setPassword=form.password1.data
            )
        homeToCreate = Home(
            # live=form.userName.data,
            doorNumber=form.doorNumber.data,
            streetName=form.road.data,
            city=form.city.data,
            postalCode=form.postalCode.data
            )
        personToCreate = Person(
            firstName=form.firstName.data,
            name=form.name.data,
            age=form.age.data
            )
        db.session.add(userToCreate)
        db.session.add(homeToCreate)
        db.session.add(personToCreate)
        db.session.commit()
    # userInfo = getUserdata(form.emailAddress.data)
    return render_template('profil.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout_page():
    logout_user()
    flash('You have been logged out !', category='info')
    # return redirect(url_for('home_page'))
    return render_template('logout.html')

