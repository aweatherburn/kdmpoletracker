from crypt import methods
from xmlrpc import client
from flask import Flask, render_template, jsonify, request
from Form.forms import ContactForm, DataForm
from random import randint
from flask_pymongo import PyMongo
from flask_mail import Mail
import json
from bson import json_util


app = Flask(__name__)
app.config['SECRET_KEY'] = '23a2097694373ea96992d3064d47ed4772375da72b911504'

app.config['MONGO_URI'] = ('mongodb+srv://aweather:bbxes123456@cluster0.wlwot.mongodb.net/FlaskTutorial?retryWrites=true&w=majority')

mail = Mail()
mongo = PyMongo()

mongo.init_app(app)
mail.init_app(app)

db = mongo.db

@app.route("/", methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def homepage():
    
    try:
        form = ContactForm()
        if request.method == 'POST':
            name = form.name.data
            email = form.email.data
            message = form.message.data
        
        print(name, email, message)
        
        # INSERT DATA INTO MONGODB
        db.clients.insert_one({
            'clientid':randint(0,1000000),
            'clientname': name,
            'clientemail': email,
            'clientmessage': message,
        })
        
        form.name.data, form.email.data, form.message.data = "", "", ""
        return render_template('about.html', form=form, success=True)
    except Exception as ex:
        print(ex)
    return render_template('homepage.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/Dashboard', methods=['POST','GET'])#, methods=['POST','GET']
def Dashboard():
    
    try:
        form = DataForm()
        if request.method == 'POST':
            location = form.location.data
            comEd = form.comEd.data
            ike = form.ike.data
            kmz = form.kmz.data
            coordinates = form.coordinates.data
            fiber_bundle = form.fiber_bundle.data
        
        print(location, comEd, ike, kmz, coordinates, fiber_bundle)
        
        # INSERT DATA INTO MONGODB
        db.L4881.insert_one({
            'loc_id':randint(0,10000000),
            'loc_loc': location,
            'loc_comed': comEd,
            'loc_ike': ike,
            'loc_kmz': kmz,
            'loc_coord': coordinates,
            'loc_fiber': fiber_bundle,
        })
        
        form.location.data, form.comEd.data, form.ike.data, form.kmz.data, form.coordinates.data, form.fiber_bundle.data = "", "", "", "", "", ""
        return render_template('Dashboard.html', form=form, success=True)
    except Exception as ex:
        print(ex)
    return render_template('Dashboard.html', form=form)

@app.route('/login')
def Login():
    return render_template('Login.html', title= 'Login')

@app.route('/L4881', methods = ['GET'])
def retrieveProject():
    poles = db.L4881.find()
    output = [{'id': pole['loc_id'], 'location': pole['loc_loc'], 'loc_comed': pole['loc_comed'], 'ike': pole['loc_ike'], 'kmz': pole['loc_kmz'], 'coord': pole['loc_coord'], 'fiber': pole['loc_fiber']} for pole in poles]
    return jsonify(output)

@app.route('/account')
def account():
    return render_template('account.html', title= 'Account')

@app.route('/pole', methods=['POST','GET'])
def Pole():
    
    # clients = db.L19342.find()
    # output = [{'id': client['loc_id'], 'location': client['loc_loc'], 'loc_comed': client['loc_comed'], 'ike': client['loc_ike'], 'kmz': client['loc_kmz'], 'coord': client['loc_coord'], 'fiber': client['loc_fiber']} for client in clients]
    # return json.dumps(output, default=json_util.default)
    return render_template('pole.html', title= 'Pole!')

@app.route('/database')
def database():

    clients = db.clients.find()
    output = [{'id': client['clientid'], 'name': client['clientname'], 'email': client['clientemail']} for client in clients]
    return jsonify(output)

@app.route('/database2')
def database2():
    try:
        if request.method == 'GET':
            poles = db.L4881.find()
            output = [{'id': pole['loc_id'], 'location': pole['loc_loc'], 'loc_comed': pole['loc_comed'], 
               'ike': pole['loc_ike'], 'kmz': pole['loc_kmz'], 'coord': pole['loc_coord'], 
               'fiber': pole['loc_fiber']} for pole in poles]
        return jsonify(output)
    except Exception as ex:
        print(ex)
    
    return render_template('database2.html')

if __name__=='__main__':
    app.run(debug=True) #debug=True