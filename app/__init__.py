import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'markbryansite.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return """
        <html>
            <head>
                <title>Mark Bryan</title>
            </head>
            <body>
                <h1>MarkBryan.io</h1>
                <p>Welcome to <em>MarkBryan.io</em></p>
            </body>
        </html>
        """

    return app
