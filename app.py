from flask import Flask, render_template, session
from models.problem import problems_bp
from models.user import user_bp
from models.analytics import analytics_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(problems_bp)
app.register_blueprint(user_bp)
app.register_blueprint(analytics_bp)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('user')
    return render_template('dashboard.html', username=username)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)