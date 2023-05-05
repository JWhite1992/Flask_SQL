from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("users.html",users=User.get_all())

# @app.route('/users')
# def users():



@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
