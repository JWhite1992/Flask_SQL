from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos= dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/edit/ninja/<int:ninja_id>')
def edit(ninja_id):
    data = {"id":ninja_id} 
    return render_template('edit.html')

@app.route('/updates/<int:ninja_id>', methods=['POST'])
def update(ninja_id):
    data = {"id":ninja_id}
    ninja.Ninja.update(request.form, ninja_id)
    return redirect ('/')

@app.route('/delete/ninjas/<int:ninja_id>')
def delete(ninja_id):
    data = {"id":ninja_id}
    ninja.Ninja.delete(data)
    return redirect('/')