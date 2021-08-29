from flask import (
    Blueprint, render_template, request
)

from app.cp.codepad import Codepad

bp = Blueprint('cp', __name__, url_prefix='/cp')


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        source = request.form['source']

        codepad = Codepad()
        result = codepad.execute(source)
        return render_template('codepad/index.html', result=result)

    return render_template('codepad/index.html', result=None)
