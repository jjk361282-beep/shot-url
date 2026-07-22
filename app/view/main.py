from apiflask import APIBlueprint
from flask import render_template
from flask_login import login_required

MainBp=APIBlueprint('main',__name__)

@MainBp.get('/')
@login_required
def index():
    return render_template('dashbord.html')
