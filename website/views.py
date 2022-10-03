from flask import Blueprint                             # std import so we can create blueprints

views = Blueprint('views', __name__)                    # std this is a load of routes inside to point to our relevant files

@views.route('/')                                       # std so defining what forward slash / does in this case calls the home function

def home():
    return "<h1>Testing the route is working</h1>"      # test to make sure its working- we also need to define the route on the __init__.py file 
