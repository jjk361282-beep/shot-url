import logging
from apiflask import APIBlueprint
from ..model import User
from flask_login import login_required,login_user,logout_user
from ..form import LoginUser,SignUser
from flask import render_template,url_for,redirect,flash

Authview=APIBlueprint("auth",__name__)

logger=logging.getLogger(__name__)

@Authview.get('/login')
@Authview.post('/login')
def login():
    form=LoginUser()
    
    if form.validate_on_submit():
        password=form.password.data
        name=form.name.data
        user=User(name=form.name.data,email=form.email.data)
        user.set_password(password)
        user.save()
        
        login_user(user,remember=True)
        
        logger.info("Tentative de connexion pour '%s'", name)
        return redirect(url_for('main.index'))
    
    return render_template('sign.html',form=form)

@Authview.get('/sign')
@Authview.post('/sign')
def sign():

    form=SignUser()
    
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data

        user=User.get_by_email(email)

        if user is not None and user.check_password(password):
            login_user(user,remember=True)
            return redirect(url_for("main.index"))
        
        flash('password or email incorrect')
        return redirect(url_for('auth.sign'))

    return render_template('login.html',form=form)

Authview.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))