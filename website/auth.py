from flask import Blueprint   #std import so we can create blueprints

auth = Blueprint('auth', __name__)   #std this is a load of routes inside to point to our relevant files

@auth.route('/login')               #std defining route for login and what function it calls
def login():                        #std  function that gets called when we visit the /login url coudl be called whatever but cleaner if stick to page name 
    return "<h1>should return when login page visited</h1>"

@auth.route('/logout')
def logout():
    return "<h1>Logout page</h1>" 

@auth.route('/sign_up')
def sign_up():
    return "<h1>SignUp Page</h1>"         