from tempfile import template
import flask
from flask import Flask, jsonify, request, make_response, redirect,render_template
from flasgger import Swagger,swag_from
from mysql.connector import cursor
import mysql.connector
from static.swagger import swagger_config,template
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
# from flask_swagger_ui import get_swaggerui_blueprint

import json
app = Flask(__name__)
app.config['DEBUG'] = True
JWTManager(app)

app.config.from_mapping(
            
            JWT_SECRET_KEY =("Bangladesh"),
            SWAGGER = {
                "title" : "Best Hotels Api",
                "uiversion" : 3
            }
        )

Swagger(app, config=swagger_config, template=template)

@app.post('/resources/v1/login')
@swag_from('./static/login.yaml')
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if email == 'admin' and password == 'admin':
#       #we will generate Jwt token Here 
        token = create_access_token(identity= email, expires_delta=timedelta(minutes=5))
        return jsonify({'token': token})
  
    else:
        return 'Invalid Credentials. Please try again.'
        

#for Databse 
@app.get('/resources/v1/hotels')
@jwt_required()
@swag_from('./static/hotel.yaml')
def resources():
    user_email = get_jwt_identity()
    if user_email == 'admin':

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
                sql=sql+"name LIKE"+f"'%{name}%'"
            else:
                sql = sql + "AND name LIKE" + f"'%{name}%'"

        if(location!=None):
            if (sql == 'SELECT * FROM data_from_web WHERE '):
                sql=sql+"location LIKE"+f"'%{location}%'"
            else:
                sql = sql + "AND location LIKE" + f"'%{location}%'"
        if(ratting!=None):
            if (sql == 'SELECT * FROM data_from_web WHERE '):
                sql=sql+"ratting="+f"'{ratting}'"
            else:
                sql = sql + "AND ratting=" + f"'{ratting}'"
        if(prices!=None):
            if (sql == 'SELECT * FROM data_from_web WHERE '):
                sql=sql+"prices >="+f"'{prices}'"
            else:
                sql = sql + "AND prices >=" + f"'{prices}'"
        if(Amenities!=None):
            if (sql == 'SELECT * FROM data_from_web WHERE '):
                sql=sql+"Amenities LIKE"+f"'%{Amenities}%'"
            else:
                sql = sql + "AND Amenities LIKE" + f"'%{Amenities}%'"
    

        query=sql
        print(query)
        cursor.execute(query)

        results = cursor.fetchall()
        print(results)
        for x in results:
            data = {
                "Hotel name": x[0],
                "location": x[1],
                "ratting": x[2],
                "prices": x[3],
                "Amenities":x[4],
                "images": x[5]
                }
            hoteldata.append(data)
            print(hoteldata)
        hoteldata.sort(key=lambda x: x["prices"])    
        json = jsonify(hoteldata)
        return json
    else:
        return 'invalid Token'    

       
app.run()