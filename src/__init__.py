from flask import Flask, jsonify, redirect
import os
from src.constants.http_status_codes import HTTP_404_NOT_FOUND

# Route imports
from src.routes.default import default_page

def create_app(test_config=None):
    app = Flask(__name__,
                instance_relative_config=True)
    
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_config)


    # Register Routes
    app.register_blueprint(default_page)


    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({
            'error': 'API Not found'
        }), HTTP_404_NOT_FOUND
    # @app.before_request
    # def before():
        # Things to be done before pre-processing


    # @app.route('/hello/', methods=['GET', 'POST'])
    # def welcome():
    #     return "Hello Wrld!"

    # @app.route('/<int:number>/')
    # def incrementer(number):
    #     return "Incremented number is " + str(number+1)

    # @app.route('/<string:name>/')
    # def hello(name):
    #     return "Hello " + name

    # @app.route('/person/')
    # def helloi():
    #     user = {'name':'Jim',
    #                     'address':'Tema'}
    #     return jsonify(user)
    
    return app;