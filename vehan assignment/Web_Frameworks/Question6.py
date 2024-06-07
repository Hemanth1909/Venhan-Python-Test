# Importing the flask
from flask import Flask

#Creating the Instance of Flask
app = Flask(__name__)

#Defining a function home for the path '/
@app.route('/')
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)
