from database.database import problem_col
from flask import Blueprint,render_template , url_for , redirect , request

problems_bp = Blueprint('problems', __name__, url_prefix='/problems')


@problems_bp.route('/add',methods=['GET','POST'])
def add_problem():
    if request.method == 'POST':
        title = request.form['title']
        platform = request.form['platform']
        difficulty = request.form['difficulty']
        problem_col.insert_one({'title':title,'platform':platform,'difficulty':difficulty})
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html')