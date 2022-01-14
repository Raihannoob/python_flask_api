import flask
from flask import Flask, jsonify, request, make_response, redirect,render_template
import jwt
import datetime
from functools import wraps
from mysql.connector import cursor
import mysql.connector
from flask_swagger_ui import get_swaggerui_blueprint

import json
app = Flask(__name__)
app.config['DEBUG'] = True


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        #need to know
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)






# Project Related Work Start From Here

@app.route('/')
def homepage():
    Heading = 'Please Login First'
    return render_template('form.html', Heading=Heading)

@app.route('/login')
def form():
    return render_template('form.html')

@app.route('/checklogin', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == 'admin' and password == 'admin':
            #we will generate Jwt token Here 
            return redirect('/dashboard')
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('form.html', error=error)
    else:
        return "Please Login First"
    return render_template("login.html")



@app.route('/dashboard')
def dashboard():
    # we will Show Swagger UI here
    return "login successfully"


@app.route('/protected')
def protected():
    #return jsonify({'message': 'Only available to people with valid tokens.'})

    return redirect("http://127.0.0.1:5000/swagger",code=302)


#for Databse 
@app.route('/data', methods=['GET'])
def data():

    hoteldata=[]

    db_connector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Scrap"
    )

    name = request.args.get('name')
    location = request.args.get('location')
    ratting = request.args.get('ratting')
    prices = request.args.get('prices')
    Amenities = request.args.get('Amenities')
    images = request.args.get('images')

    cursor = db_connector.cursor()

    sql= "SELECT * FROM data_from_web WHERE "
    

    if(name!=None):
        if(sql=='SELECT * FROM data_from_web WHERE '):
            sql=sql+"name="+f"'{name}'"
        else:
            sql = sql + "AND name=" + f"' {name}'"

    if(location!=None):
        if (sql == 'SELECT * FROM data_from_web WHERE '):
            sql=sql+"location="+f"'{location}'"
        else:
            sql = sql + "AND location=" + f"'{location}'"
    if(ratting!=None):
        if (sql == 'SELECT * FROM data_from_web WHERE '):
            sql=sql+"ratting="+f"'{ratting}'"
        else:
            sql = sql + "AND ratting=" + f"'{ratting}'"
    if(prices!=None):
        if (sql == 'SELECT * FROM data_from_web WHERE '):
            sql=sql+"prices>="+f"'{prices}'"
        else:
            sql = sql + "AND prices=" + f"'{prices}'"
    if(Amenities!=None):
        if (sql == 'SELECT * FROM data_from_web WHERE '):
            sql=sql+"Amenities>="+f"'{Amenities}'"
        else:
            sql = sql + "AND Amenities=" + f"'{Amenities}'"
    if(images!=None):
        if (sql == 'SELECT * FROM data_from_web WHERE '):
            sql=sql+"images="+f"'${images}'"
        else:
            sql = sql + "AND images=" + f"'${images}'"

    query=sql
    print(query)
    cursor.execute(query)

    results = cursor.fetchall()

    for x in results:
        data = {
            "name": x[0],
            "location": x[1],
            "ratting": x[2],
            "prices": x[3],
            "Amenities":x[4],
            "images": x[5]
            }
        hoteldata.append(data)
        print(hoteldata)
    json = jsonify(hoteldata)
    return json

       
app.run()