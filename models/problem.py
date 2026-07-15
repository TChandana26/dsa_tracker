from database.database import problem_col,user_col
from flask import Blueprint, render_template, request, redirect, url_for , session , jsonify



# Blueprint
problems_bp = Blueprint(
    'problem',
    __name__,
    url_prefix='/problem'
)

# ---------------- Add Problem ----------------
@problems_bp.route('/add', methods=['GET', 'POST'])
def add_problem():

    if "user" not in session:
        return redirect(url_for("user.login"))
    
    if request.method == 'POST':
        title = request.form['title']
        platform = request.form['platform']
        difficulty = request.form['difficulty']
        problem_link = request.form['problem_link']
        notes = request.form['notes']

        problem_col.insert_one({
            'username' : session['user'],
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

    if "user" not in session:
        return redirect(url_for("user.login"))
    
    problems = list(problem_col.find({"username": session["user"]}))

    return render_template(
        'view_problem.html',
        problems=problems
    )

#----------------topics-----------------------
@problems_bp.route('/topic')
def topic():

    if "user" not in session:
        return redirect(url_for("user.login"))

    username = session["user"]

    user = user_col.find_one({"username": username})

    completed_topics = user.get("completed_topics", [])

    return render_template(
        "topic.html",
        completed_topics=completed_topics
    )
#-----------------checkboxes saved-------------------------

@problems_bp.route("/save_topic", methods=["POST"])
def save_topic():

    if "user" not in session:
        return redirect(url_for("user.login"))

    data = request.get_json()

    username = session["user"]
    

    topic = data["topic"]

    checked = data["checked"]

    if checked:

        user_col.update_one(
            {"username": username},
            {"$addToSet": {"completed_topics": topic}}
        )

    else:

        user_col.update_one(
            {"username": username},
            {"$pull": {"completed_topics": topic}}
        )

    return jsonify({"success": True})