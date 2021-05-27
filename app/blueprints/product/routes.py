from . import bp as product
from app import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Products



@product.route('/product', methods = ['GET', 'POST'])
@login_required
def allproduct():
    title = 'Products'
    product = Products.query.all()
    return render_template('product.html', title=title, product=product)



@product.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Products.query.get_or_404(product_id)
    title = "Product Detail"
    name = product.title
    amount = product.amount
    desc = product.description

    return render_template('productdetail.html', title=title, amount=amount, desc=desc, name=name, product=product)