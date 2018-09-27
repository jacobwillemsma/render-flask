from flask import render_template, Blueprint, request, redirect, url_for, flash
from project import db
from project.models import Item
from .forms import AddItemForm

# config
items_blueprint = Blueprint('items', __name__, template_folder='templates')


# helper functions
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'info')


# routes
@items_blueprint.route('/')
def index():
    all_items = Item.query.all()
    return render_template('items.html', items=all_items)

@items_blueprint.route('/add', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_item = Item(form.item_title.data, form.item_description.data, form.item_comment.data)
            db.session.add(new_item)
            db.session.commit()
            flash('New item, {}, added!'.format(new_item.item_title), 'success')
            return redirect(url_for('items.index'))
        else:
            flash_errors(form)
            flash('ERROR! Item was not added.', 'error')

    return render_template('add_item.html',
                           form=form)
