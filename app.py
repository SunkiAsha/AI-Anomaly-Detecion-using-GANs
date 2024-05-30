import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3

import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime

warnings.filterwarnings('ignore')



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/home2')
def home2():
	return render_template('home1.html')

@app.route('/home3')
def home3():
	return render_template('home2.html')


@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')




@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    otp = random.randint(1000,5000)
    print(otp)
    msg = EmailMessage()
    msg.set_content("Your OTP is : "+str(otp))
    msg['Subject'] = 'OTP'
    msg['From'] = "evotingotp4@gmail.com"
    msg['To'] = email
    
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("evotingotp4@gmail.com", "xowpojqyiygprhgr")
    s.send_message(msg)
    s.quit()
    return render_template("val.html")

@app.route('/predict_lo', methods=['POST'])
def predict_lo():
    global otp, username, name, email, number, password
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        if int(message) == otp:
            print("TRUE")
            con = sqlite3.connect('signup.db')
            cur = con.cursor()
            cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
            con.commit()
            con.close()
            return render_template("signin.html")
    return render_template("signup.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signin.html")





@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    #model = joblib.load('models/nsl_binary.sav')
    model1 = joblib.load('model_nsl.sav')
    #predict = model.predict(final4)
    predict1 = model1.predict(final4)

    if  predict1 == 0:
        output = 'There is an Attack Detected, Attack Type is DoS!'
    elif predict1 == 1:
        output = 'There is an Attack Detected, Attack Type is Probe!'
    elif predict1 == 2:
         output = 'There is an Attack Detected, Attack Type is U2R!'
    elif predict1 == 3:
        output = 'There is an Attack Detected, Attack Type is R2L!'
    elif predict1 == 4:
         output = 'There is no Attack Detected, it is Normal!'
         

    return render_template('prediction.html', output=output)


@app.route('/predict1',methods=['POST'])
def predict1():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    #model = joblib.load('models/nsl_binary.sav')
    model1 = joblib.load('model_unsw.sav')
    #predict = model.predict(final4)
    predict1 = model1.predict(final4)

    if  predict1==1:
        output = 'There is an Attack Detected, Attack Type is either DoS/Reconnaissance/Others!'
    elif predict1 == 0:
    
        output = 'There is no Attack Detected, it is Normal!'

    return render_template('prediction1.html', output=output)


@app.route('/predict2',methods=['POST'])
def predict2():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    #model = joblib.load('models/nsl_binary.sav')
    model1 = joblib.load('model_iot.sav')
    #predict = model.predict(final4)
    predict1 = model1.predict(final4)

    if  predict1==1:
        output = 'There is an Attack Detected, Attack Type is either DoS/Injection/others!'
    elif predict1 == 0:
    
        output = 'There is no Attack Detected, it is Normal!'

    return render_template('prediction2.html', output=output)



@app.route("/notebook1")
def notebook1():
    return render_template("NSL-KDD.html")

@app.route("/notebook2")
def notebook2():
    return render_template("UNSW-NB15.html")

@app.route("/notebook3")
def notebook3():
    return render_template("IOT-23.html")



if __name__ == "__main__":
    app.run(debug=True)
