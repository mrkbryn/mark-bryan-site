import os

from flask import Flask, render_template

from app import mock_data
from app.db import get_db


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
        return render_template('index.html')

    @app.route('/research')
    def research():
        return render_template('research.html', research=mock_data.research)

    @app.route('/resume')
    def resume():
        # Fetch experiences from database and parse into a UI view...
        # Ignore my terrible data model for now...
        db = get_db()
        experience_view = []
        experiences = db.execute(
            'SELECT e.id, e.name, e.title, e.location, e.dates, e.body'
            ' FROM experience e'
            ' ORDER BY created ASC'
        ).fetchall()
        for e in experiences:
            experience_view.append({
                'id': e['id'],
                'name': e['name'],
                'title': e['title'],
                'location': e['location'],
                'dates': e['dates'],
                'notes': e['body'].split('|'),
            })

        education_view = []
        education = db.execute(
            'SELECT e.id, e.name, e.location, e.dates, e.body'
            ' FROM education e'
            ' ORDER BY created ASC'
        ).fetchall()
        for e in education:
            education_view.append({
                'id': e['id'],
                'name': e['name'],
                'location': e['location'],
                'dates': e['dates'],
                'notes': e['body'].split('|'),
            })

        return render_template('resume.html',
                               experience=experience_view,
                               education=education_view)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    return app
