import json
from consulate.connectToRedis import connection_redis
from consulate import bcrypt
from consulate import loginManager
from flask_login import UserMixin, login_user
r = connection_redis()

def createUser(form):
    dict = {
    'userName': form.userName.data,
    'email': form.emailAddress.data,
    'password': bcrypt.generate_password_hash(form.password1.data).decode("utf-8"), 
    'firstName': "",
    'name': "",
    'age': "",
    'doorNumber': "",
    'road': "",
    'city': "",
    'postalCode': "",
    'phoneNumber': "",
    'passportNumber': "",
    'passportExpirationDate': "",
    'passportCreationDate': "",
    'hadVisaBefore': '',
    'askedVisa': '',
    'askedVisaValidated': '',
    'askedVisaRefused': '',
    'participantToLoterie': ''
    }  
    fileName = "newUser.json"
    otfile = open(fileName, "w")
    json.dump(dict, otfile)
    otfile.close()

    listKeys = r.keys("*")
    listKeys.sort()
    with open("newUser.json") as access_json:
        data = json.load(access_json)
        if listKeys == []:
            print("vide")
            r.json().set('1', ".", data)
        else:
            r.json().set(str(int(listKeys[-1])+1), ".", data)
    
def checkUserConnexion(form):
    listKeys = r.keys("*")
    for key in listKeys:
        # print("redis: ", r.json().get(key, "email"), r.json().get(key, "password"))
        # print("user: ", form.emailAddress.data, form.password.data)
        if r.json().get(key, "userName") == form.userName.data and bcrypt.check_password_hash(
            r.json().get(key, "password"), form.password.data
        ):
            return True
    return False

def getUserdata(emailAddressUser):
    listKeys = r.keys("*")
    for key in listKeys:
        if r.json().get(key, "email") == emailAddressUser:
            return r.json().get(key)
        
@loginManager.user_loader
def load_user(user_id):
        return r.json().get(user_id)

def getUserId(userName):
    listKeys = r.keys("*")
    for key in listKeys:
        if r.json().get(key, "userName") == userName:
            return r.json().get(key)