from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import get_db

bp = Blueprint('resume', __name__, url_prefix='/resume')


@bp.route('/')
def index():
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

    return render_template('resume/index.html', experience=experience_view, education=education_view)
