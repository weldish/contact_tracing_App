from app import app, db
from flask import render_template, url_for, redirect, request
from app.forms import AddForm,UploadTestResult
from app.models import Todo, User, Exposures
import random


@app.route("/")
@app.route("/home")
def home():
    infected_users= User.query.all()
    return render_template("home.html", infected_users=infected_users)


@app.route("/add", methods=["GET", "POST"])
def add():

    form=AddForm()
    if form.validate_on_submit():
        random_number=random.randint(1, 1000)   # creating a randon key or beacon
        user_1=User(username=form.name.data, infected=False, beacon_key=form.name.data + str(random_number))
        db.session.add(user_1)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)   # provinding the user with a form to input his to do list


@app.route("/incomplete")                  #route for the incomplete page
def incomplete():
    active_lists=Todo.query.filter_by(complete=False).all()
    return render_template("incomplete.html", active_lists=active_lists)

@app.route("/complete")                  #route for the ccomplete page
def complete():
    inactive_lists=Todo.query.filter_by(complete=True).all()
    return render_template("completed.html", inactive_lists=inactive_lists)

@app.route("/tick/<int:todo_id>")        # marks the task if completed
def tick(todo_id):
    tiked_list=Todo.query.filter_by(id=todo_id).first()
    tiked_list.complete=not tiked_list.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/Upload", methods=["GET", "POST"])
def Upload():

    form=UploadTestResult()
    if form.validate_on_submit():
        updated_status=User.query.filter_by(username=form.name.data).first();  #querying for the user
        updated_status.infected=not updated_status.infected       #updating the users status
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form)



@app.route("/delete/<int:todo_id>")      # deletes the selected task
def delete(todo_id):
    deleted_list=Todo.query.filter_by(id=todo_id).first()
    db.session.delete(deleted_list)
    db.session.commit()
    return redirect(url_for("home"))
