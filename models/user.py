from database.database import user_col
from flask import Blueprint, render_template , request , url_for , redirect , session , flash
from werkzeug.security import generate_password_hash, check_password_hash
print("LOADED USER.PY")

user_bp = Blueprint('user' , __name__ , url_prefix = '/user')

@user_bp.route('/login' , methods = ['POST' , 'GET'])



def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            user = user_col.find_one({'username': username})
            if user and check_password_hash(user['password'], password):
                session['user'] = username
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid Details")
        except Exception as e:
            print("Login error:", e)
            return "Internal Server Error", 500
    return render_template('login.html')


@user_bp.route('/register' , methods =['POST' , 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        user_col.insert_one({'username' : username , 'password' : password})
        print(username,password)
        return redirect(url_for('user.login'))
    return render_template('register.html')


@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))

