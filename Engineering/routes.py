from crypt import methods
from Engineering import app
from flask import Flask,render_template,request,jsonify
from flask_pymongo import PyMongo
#from Form.forms import DataForm, ContactForm
from random import randint
from flask_mail import Mail,Message
#import pymongo


    
headings = ("Location", "Instruction", "  ", "AS8 Codes", "Quantity")
data = (
    ("120", "R", "", "PJT60-2-T-T", "1"),
    ("120", "R", "", "R-ANCH-O", "1"),
    ("120", "R", "", "R-ANCHG-O", "1")
    # ("120", "R", "", "R-PRIDE-O", "1"),
    # ("120", "R", "", "R-SECDE-O", "1"),
    # ("120", "R", "", "R-WA-O", "1")
)

# mongo = PyMongo()
# mail = Mail()


    

# mongo.init_app(app)
# mail.init_app(app)

#db = mongo.db   

@app.route('/')#, methods=['POST','GET']

@app.route('/home')#, methods=['POST','GET']
def homepage():
    
    return render_template('homepage.html', title= 'Home Page')

@app.route('/about')#, methods=['POST','GET']
def about():
    # form = DataForm()
    # if request.method == 'POST':
    #     location = form.location.data
    #     comed = form.comed.data
    #     ike = form.ike.data
    #     kmz = form.kmz.data
    #     lonlat = form.lonlat.data
    #     fiber = form.fiber.data
        
    #     #INSERT DATA INTO MONGODB
    #     db.clients.insert_one({
    #         'poleid':randint(0,1000000),
    #         'polelocation': location,
    #         'polecomed': comed,
    #         'poleike': ike,
    #         'polekmz': kmz,
    #         'polelonlat': lonlat,
    #         'polefiber': fiber,
    #     })
    #     form.location.data, form.comed.data, form.ike.data, form.kmz.data, form.lonlat.data, form.fiber.data = '','','','','',''
    #     return render_template('index.html', form=form, success=True)
    return render_template('about.html', title= 'About')

@app.route('/login')
def Login():
    return render_template('Login.html', title= 'Login')

@app.route('/account')
def account():
    return render_template('account.html', title= 'Account', headings=headings, data=data)

@app.route('/pole')
def Pole():
    return render_template('pole.html', title= 'Pole!')

# @app.route("/database")
# def database():
#     clients = pymongo.MongoClient("mongodb+srv://aweather:bbxes123456@cluster0.wlwot.mongodb.net/FlaskTutorial?retryWrites=true&w=majority")['FlaskTutorial']['clients']
#     clients = clients.find()
#     output = [{'id': client['clientid'], 'name':client['clientname'], 'email': client['clientemail'], 'message':client['clientmessage']} for client in clients]
#     return jsonify(output)
#     #return render_template('database.html', clients = Clients.query.all())

if __name__=='__main__':
    app.run(debug=True)