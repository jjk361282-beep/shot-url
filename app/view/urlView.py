from apiflask import APIBlueprint
from flask_login import login_required,current_user
from ..utils import shorten
import sqlalchemy as sa
from flask import redirect,render_template,request
from ..model import Url
from ..db import db

UrlView=APIBlueprint("url",__name__)

@UrlView.get('/<slug>')
def index(slug):
    url=db.session.scalar(sa.select(Url).where(
        Url.slug==slug
    ))
    if url is not None:
        print(request.remote_addr)
        url.nb_click=+1
        db.session.commit()
        return redirect(url.original_url)
    return render_template('index.html')

@UrlView.post('/')
@login_required
def createUrl():
    links=request.form.get('url')

    print(dict(request.form))
    slug=shorten(links)
    url=Url(original_url=links,slug=slug,id_author=current_user.id)
    url.save()
    return ""