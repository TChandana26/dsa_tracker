from database.database import problem_col
from flask import Blueprint, render_template, request, redirect, url_for




# Blueprint
problems_bp = Blueprint(
    'problem',
    __name__,
    url_prefix='/problem'
)

# ---------------- Add Problem ----------------
@problems_bp.route('/add', methods=['GET', 'POST'])
def add_problem():

    if request.method == 'POST':
        title = request.form['title']
        platform = request.form['platform']
        difficulty = request.form['difficulty']
        problem_link = request.form['problem_link']
        notes = request.form['notes']
        print(request.form)
        problem_col.insert_one({
            'title': title,
            'platform': platform,
            'difficulty': difficulty,
            'problem_link' : problem_link,
            'notes':notes
        })
        return redirect(url_for('problem.view_problem'))

    return render_template('problem.html')


# ---------------- View Problems ----------------
@problems_bp.route('/view', methods=['GET'])
def view_problem():

    problems = list(problem_col.find())

    return render_template(
        'view_problem.html',
        problems=problems
    )

