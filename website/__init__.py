from flask import Flask                             # importing flask for use last Flask is Case-Sensitive

def create_app():                                   # std         
    app = Flask(__name__)                           # std    
    app.config['SECRET_KEY'] = 'rweewwerr'           # encryption key done use for production

    from .views import views                        # std we are telling our app we have blueprints so importing them 
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')  # std we are registering our blueprints   slash means no prefix....
    app.register_blueprint(auth, url_prefix='/')

    return app                                      # std