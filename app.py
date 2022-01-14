import flask
from flask import Flask, jsonify, request, make_response, redirect,render_template
import jwt
import datetime
from functools import wraps
from mysql.connector import cursor
import mysql.connector

import json
app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/regestration', methods = ['POST', 'GET'])
# def regestration():
#     db_connector = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="flask"
#     )
#     if request.method == 'GET':
#         return "Login via the login Form"
     
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = db_connector.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         db_connector.commit()
#         cursor.close()
#         return f"Done!!"

# Token Decorator
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 403

#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 403

#         return f(*args, **kwargs)

#     return decorated
# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]


# @app.route('/')
# def index():
#     return redirect('http://127.0.0.1:5000/login')

# @app.route('/login')
# def login():
#     auth = request.authorization

#     # if auth and auth.password == '1234':
#     token = jwt.encode({'user': 'raihan', 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=50)},
#                            app.config['SECRET_KEY'])
#     return jsonify({'token': token})
#     # return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm:"Login Required"'})


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)
# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."
#     results = []
#     for book in books:
#         if book['id'] == id:
#             results.append(book)
#     return jsonify(results) 
# @app.route('/data', methods=['GET'])
# def house():
#    # title bedroom sleeps bathroom price location
#     hoteldata=[]

#     db_connector = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="Scrapping"
#     )


#     title = request.args.get('title')
#     bedroom = request.args.get('bedroom')
#     sleep = request.args.get('sleeps')
#     bathroom = request.args.get('bathroom')
#     price = request.args.get('price')
#     location = request.args.get('location')

#     cursor = db_connector.cursor()
# # sleep  	bedroom  	bathroom  	price title
#     sql= "SELECT * FROM datatable WHERE "
#     valudata=0

#     if(title!=None):
#         if(sql=='SELECT * FROM datatable WHERE '):
#             sql=sql+"title="+f"'{title}'"
#         else:
#             sql = sql + "AND title=" + f"' {title}'"

#     if(location!=None):
#         if (sql == 'SELECT * FROM datatable WHERE '):
#             sql=sql+"location="+f"'{location}'"
#         else:
#             sql = sql + "AND location=" + f"'{location}'"
#     if(bedroom!=None):
#         if (sql == 'SELECT * FROM datatable WHERE '):
#             sql=sql+"bedroom="+f"'{bedroom}'"
#         else:
#             sql = sql + "AND bedroom>=" + f"'{bedroom}'"
#     if(bathroom!=None):
#         if (sql == 'SELECT * FROM datatable WHERE '):
#             sql=sql+"bathroom>="+f"'{bathroom}'"
#         else:
#             sql = sql + "AND bathroom>=" + f"'{bathroom}'"
#     if(sleep!=None):
#         if (sql == 'SELECT * FROM datatable WHERE '):
#             sql=sql+"sleep>="+f"'{sleep}'"
#         else:
#             sql = sql + "AND sleep>=" + f"'{sleep}'"
#     if(price!=None):
#         if (sql == 'SELECT * FROM datatable WHERE '):
#             sql=sql+"price>="+f"'${price}'"
#         else:
#             sql = sql + "AND price>=" + f"'${price}'"


#     # query = ("SELECT * FROM datatable WHERE location ="+f"'{location}'  OR price=" + f"'{price}' OR bedroom=" + f"'{bedroom}'OR bathroom=" + f"'{bathroom}' OR sleep=" + f"'{sleeps}'")
#     query=sql
#     print(query)
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for x in results:
#         data = {
#             "Title": x[0],
#             "Location": x[1],
#             "Sleeps": x[2],
#             "Bedrooms": x[3],
#             "Bathrooms": x[4],
#             "Price": x[5],
#             "Picture": {
#                 "Picture_1": x[6],
#                 "Picture_2": x[7],
#                 "Picture_3": x[8],
#             }

#         }
#         hoteldata.append(data)

#     # Json = json.dumps(hoteldata, indent=4)


#     hoteldata.sort(key=lambda x: x["Price"])


#     Json = json.dumps(hoteldata, indent=4)
#     print(Json)
#     # print(title, bedroom, sleeps, location)
#     return Json






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

#for Databse 
@app.route('/data', methods=['GET'])
def house():
   # name location ratting prices Amenities images
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
    valudata=0

    if(name!=None):
        if(sql=='SELECT * FROM data_from_web WHERE '):
            sql=sql+"name="+f"'{name}'"
        else:
            sql = sql + "AND title=" + f"' {name}'"

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
         # name location ratting prices Amenities images
        data = {
            "name": x[0],
            "location": x[1],
            "ratting": x[2],
            "prices": x[3],
            "Amenities":x[4],
            "images": x[5]
            }
        hoteldata.append(data)
    json = jsonify(hoteldata)
    return json

       
app.run()