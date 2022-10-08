from flask import Flask                             # importing flask for use last Flask is Case-Sensitive

def create_app():                                   # std         
    app = Flask(__name__)                           # std    
    app.config['SECRET_KEY'] = 'rweewwerr'           # std encryption key don't use for production

    from .views import views                        # std importing blueprints for use
    from.auth import auth                           #std importing blueprints for use

    app.register_blueprint(views, url_prefix='/')     # std registering views blueprint  the forward slashes is indicating pages reference from the root.... 
    app.register_blueprint(auth, url_prefix='/')     # std registering auth blueprint 

    return app                                      # std