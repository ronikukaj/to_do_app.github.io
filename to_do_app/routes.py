from flask import render_template, redirect, url_for, request
from to_do_app import app, db
from to_do_app.forms import SubmitForm
from to_do_app.models import ToDo, Finished


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item_ = request.form.get("holder")
        print(item_)
        if item_ != None:
            db_item = ToDo(item=item_)
            db.session.add(db_item)
            db.session.commit()
    to_do_items = ToDo.query.all()
    finished_items = Finished.query.all()

    return render_template('index.html', title='TO DO APP', to_do_items=to_do_items, finished_items=finished_items)

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item = ToDo.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/finish/<int:item_id>')
def finish(item_id):
    item_todo = ToDo.query.get_or_404(item_id)
    finish_item = Finished(item=item_todo.item)
    db.session.add(finish_item)
    db.session.delete(item_todo)
    db.session.commit()
    return redirect(url_for('home'))
