from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
#from werzeug.exceptions import abort

bp = Blueprint('weather', __name__)

@bp.route('/')
def index():
    return render_template('weather/index.html')
