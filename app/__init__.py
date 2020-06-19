import os

from flask import Flask


def create_app(test_config=None):
    """Builder of the app

    @param test_config: ???
    @return: the app instance
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # Load the default config
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    # allows to load a specific config
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello", methods=['POST', 'GET'])
    def hello():
        return "Hello, World!"

    # Import the function in the main function
    from app import main
    app.register_blueprint(main.bp)


    return app

