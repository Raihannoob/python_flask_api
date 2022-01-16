# python_flask_api
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
- Once you have activated your programming environment, install Flask using the pip install command:
 ```bash
  pip install flask
  pip install flask_swagger_ui
  pip install PyJWT
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
