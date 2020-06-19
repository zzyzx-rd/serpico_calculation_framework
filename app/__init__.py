import os

from flask import Flask
import redis
import time


def create_app(test_config=None):
    """Builder of the app

    @param test_config: ???
    @return: the app instance
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cache = redis.Redis(host='redis', port=6379)
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

    def get_hit_count():
        retries = 5
        while True:
            try:
                return cache.incr('hits')
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                time.sleep(0.5)

    @app.route('/')
    def hello():
        count = get_hit_count()
        return 'Hello World! I have been seen {} times.\n'.format(count)

    # Import the function in the main function
    from app import main
    app.register_blueprint(main.bp)

    return app
