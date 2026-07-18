# 🚀 DSA Tracker

A **Flask + MongoDB** based web application that helps students organize, track, and improve their Data Structures & Algorithms (DSA) practice. It provides a centralized platform to manage coding problems, track topic-wise progress, write notes, and visualize learning analytics.

---

## 📌 Features

### 👤 User Authentication
- Secure User Registration & Login
- Password hashing using Werkzeug
- Session-based authentication

### 📝 Problem Management
- Add coding problems
- Edit and delete problems
- Store problem details:
  - Problem Title
  - Platform (LeetCode, CodeChef, HackerRank, etc.)
  - Difficulty
  - Topic
  - Notes
  - Solution

### 📚 Topic Checklist
- Track completed DSA topics
- User-specific progress
- Persistent checklist stored in MongoDB

### 📊 Analytics Dashboard
- Total problems solved
- Difficulty-wise distribution
- Topic-wise statistics
- Interactive charts using Chart.js
- Progress overview

### 📖 Notes Management
- Save notes for every problem
- Update notes anytime
- View notes separately

### 🎨 Responsive UI
- Clean dashboard
- Modern cards
- Sidebar navigation
- Responsive layout
- Font Awesome icons

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| MongoDB Atlas | Database |
| PyMongo | MongoDB Driver |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Interactivity |
| Chart.js | Analytics Charts |
| Jinja2 | Template Engine |

---

# 📂 Project Structure

```
dsa_tracker/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── database/
│   ├── database.py
│
├── routes/
│   ├── user.py
│   ├── problems.py
│   └── analytics.py
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── problem.html
│   ├── view_problem.html
│   
├── static/
│   ├── style.css
|   |__
|   static/style1.css static/style2.css static/style3.css static/topic.css static/view.css
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/dsa-tracker.git
```

```bash
cd dsa-tracker
```

---

## 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create a `.env` file

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
```

---

## 5️⃣ Run the project

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

> Add screenshots here after deployment.

Example:

```
Home Page

Dashboard

Add Problem

Analytics

Notes
```

---

# 📈 Future Improvements

- 🔥 Daily Coding Streak
- 📅 Coding Calendar
- 📊 Advanced Analytics
- 🏆 Leaderboard
- 📱 Mobile Responsive Design
- 🔍 Search & Filter Problems
- 📤 Export Notes as PDF
- 🌙 Dark Mode
- 🤖 AI-based Problem Recommendations
- 💡 AI-generated Hints & Explanations

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Chandana T**

- 🎓 B.Tech Student
- 💻 Passionate about AI, Full Stack Development & DSA
- 🚀 Building projects to improve coding skills

---

## ⭐ If you found this project useful, please give it a Star!

Happy Coding! 🚀