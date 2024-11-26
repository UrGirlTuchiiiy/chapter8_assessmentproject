from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import AddproductForm, RegisterForm


@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been registered {form.username.data}')
        return redirect(url_for('/addproduct'))
    return render_template('register.html', title='Register Page', form=form)

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    """Addproduct URL"""
    form = AddproductForm()
    if form.validate_on_submit():
        flash(f'Your product has been saved')
        return redirect(url_for('index'))
    return render_template('addproduct.html', title='Add_Product', form=form)
    