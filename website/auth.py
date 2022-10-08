from flask import Blueprint, render_template   #std import so we can create blueprints

auth = Blueprint('auth', __name__)   #std this is a load of routes inside to point to our relevant files

@auth.route('/login')               #std defining route for login and what function it calls
def login():                        #std  function that gets called when we visit the /login url coudl be called whatever but cleaner if stick to page name 
    return render_template("login.html", user="Tim") 

@auth.route('/logout')
def logout():
    return "<h1>Logout page</h1>"    #std we wouldn't  really do this we would however instead render HTML via the templates folder using JINGA.... 

@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html", user="Tim")  #std rendering our template...     