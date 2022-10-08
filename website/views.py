from flask import Blueprint ,render_template                             # std import so we can create blueprints and render_template so we can use templates such as base.html 

views = Blueprint('views', __name__)                    # std this is a load of routes inside to point to our relevant files

@views.route('/')                                       # std so defining the view  what forward slash / does in this case calls the home function
def home():
    return render_template("home.html")      # std returns out home.html in templates - render template 
