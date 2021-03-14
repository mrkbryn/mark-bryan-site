import json
from flask import Blueprint, render_template, current_app

bp = Blueprint('resume', __name__, url_prefix='/resume')


@bp.route('/')
def index():
    with current_app.open_resource('resume.json') as f:
        data = json.load(f)
    return render_template('resume/index.html', resume=data)
