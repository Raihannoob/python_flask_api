<h1 align="center">python_Flask_api  👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

#### Features
- It takes any or all parameters from query string like Hotel name,price,location,ratting,Amminities and gives api data.
- For authentication you have to go http://127.0.0.1:5000/ this route and  appear a Swagger UI there you will get a post/login option click there and provide your account information where usernaem is "admin" password is "admin" .
- After login Successfully you Will get a JWt token which is valid for 5 min.
- Then go to get hotel option and there you saw a input box for authorization Which is must required for access data.so you have to give the Jwt token to access.jwt Token formet : Bearer your_token and give  parameter and response data if available sorted by prices.

#### How complete this project
- First You should know besic knowledge about python,then you should switch to flask documentation I read several documentation about flask here is the documentation link https://www.tutorialspoint.com/flask/index.htm ,https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
- So after finishing the flask besic then switch to Flask Api how it wroks by reading this doucumentation https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask it will give you a proper idea about flask api.
- After that we need a JWT authentication for our api for security reason so try to grab some idea about Jwt authentication by reading this documentation https://flask-jwt-extended.readthedocs.io/en/stable/ or watch this video from youtube https://www.youtube.com/watch?v=AsQ8OcVvK3U
- Now we need a ui to test our api so now try to grab some idea about swagger Ui by reading this https://swagger.io/specification/ I will recommend you for swagger try to find some project in swagger and edit json file to understand swagger ui or you can use editor.swagger.io for swagger json knowledge  

#### prerequisite
- Install Python
- Install XAMPP

 #### step 1
 - install virtual env by this command 
 ```bash
   virtualenv venv
```
#### step 2
- active venv by this command 
 ```bash
  source venv/bin/activate
```
#### step 3
- Once you have activated your programming environment, install this packages by this  command:
 ```bash
  pip install flask
  pip install flask_swagger_ui
  pip install mysql-connector-python
  pip install Flask-JWT-Extended
  pip install flasgger

```

- Creating a Simple Application app.py
#### step 4
- while in your flask_app directory with your virtual environment activated, tell Flask where to find the application (app.py in your case) using the FLASK_APP environment variable with the following command:
```bash
  export FLASK_APP=app
```

- Then specify that you want to run the application in development mode (so you can use the debugger to catch errors) with the FLASK_ENV environment variable:
```bash
  export FLASK_ENV=development

```
#### step 5
- Lastly,inatall requirements.txt:

```bash
pip install -r requirements.txt python3 app.py

```
#### step 6
- Lastly, run the application using the flask run command:

```bash
 flask run

```
#### Database Creation

- Import data_from_web.sql
- If the data_from_web.sql does't work then create table using the query bellow

CREATE TABLE `data_from_web` (
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `ratting` varchar(255) NOT NULL,
  `prices` int(255) NOT NULL,
  `Amenities` varchar(255) NOT NULL,
  `images` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

- If table doesn't work then Import the (Scrap.sql) provided with the cloned folder into the database. 


## Feedback

If you have any feedback, please reach out to us at raihan.tanvir961@gmail.com


## 🚀 About Me
I'm a Softwere Engineer 

