from database.database import user_col
from flask import Blueprint, render_template , request , url_for , redirect , session
from werkzeug.security import generate_password_hash, check_password_hash
print("LOADED USER.PY")

user_bp = Blueprint('user' , __name__ , url_prefix = '/user')

@user_bp.route('/login' , methods = ['POST' , 'GET'])



def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_col.find_one({'username' : username})
        if user and check_password_hash(user['password'],password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Details"
    return render_template('login.html')


@user_bp.route('/register' , methods =['POST' , 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        user_col.insert_one({'username' : username , 'password' : password , 'email' : email})
        print(username,password,email)
        return redirect(url_for('user.login'))
    return render_template('register.html')




