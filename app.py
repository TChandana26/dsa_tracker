from flask import Flask, render_template, url_for, request, redirect , session
from models.problem import problems_bp
from models.user import user_bp
from models.analytics import analytics_bp

app = Flask (__name__)
app.register_blueprint(problems_bp)
app.register_blueprint(user_bp)
app.register_blueprint(analytics_bp)

app.secret_key = "my_secret_key"

print(app.url_map)
for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint} URL: {rule}")

@app.route('/')
def base():
   return render_template('base.html')


@app.route('/dashboard')
def dashboard():
   print("SESSION DATA:", session)
   username = session.get('user')
   return render_template('dashboard.html',username=username) 


if __name__ == "__main__" :
    app.run(debug=True,use_reloader=False)