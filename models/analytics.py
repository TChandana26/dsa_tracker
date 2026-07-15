from flask import Blueprint, render_template, Response , session , request , url_for , redirect
from collections import Counter
from io import BytesIO
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
from database.database import problem_col

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("user.login"))

    username = session["user"]

    problems = list(problem_col.find({"username": username}))

    recent = list(problem_col.find({"username": username}).sort("_id", -1).limit(5))
    username = session.get("user")

    total = len(problems)
    difficulty = Counter([p["difficulty"] for p in problems])

    return render_template(
        "dashboard.html",
        username=username,
        problems=recent,
        total=total,
        easy=difficulty.get("Easy", 0),
        medium=difficulty.get("Medium", 0),
        hard=difficulty.get("Hard", 0),
    )

@analytics_bp.route("/pie_chart")
def pie_chart():

    if "user" not in session:
        return redirect(url_for("user.login"))

    problems = list(problem_col.find({"username": session["user"]}))

    difficulty = Counter([p["difficulty"] for p in problems])

    labels = ["Easy", "Medium", "Hard"]

    sizes = [
        difficulty.get("Easy", 0),
        difficulty.get("Medium", 0),
        difficulty.get("Hard", 0)
    ]

    plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")

    img = BytesIO()

    plt.savefig(img, format="png")
    plt.close()

    img.seek(0)

    return Response(img.getvalue(), mimetype="image/png")

