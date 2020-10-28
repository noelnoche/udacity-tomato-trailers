"""This file initializes the application and brings together all of the 
various components.  
"""
def create_app():
    """Factory function that initializes the Flask application context.
    
    Imports Flask and blueprints and sets configuration values.
    """
    from flask import Flask
    from trailersweb.cache import cache
    

    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
        
    with app.app_context():
        from trailersweb.views import bp_views        
        app.register_blueprint(bp_views, url_prefix="/trailersweb")
        cache.init_app(app)

    return app


app = create_app()
