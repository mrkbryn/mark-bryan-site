import json
from flask import Blueprint, render_template, current_app

bp = Blueprint('research', __name__, url_prefix='/research')


@bp.route('/')
def index():
    with current_app.open_resource('research.json') as f:
        data = json.load(f)
    return render_template('research/index.html', research=data)
