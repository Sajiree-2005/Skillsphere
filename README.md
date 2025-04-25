# Skillsphere
# 🌐 SkillSphere - Online Course Recommendation Web App

SkillSphere is a sleek and modern Flask-based web application that helps users discover **top-rated, paid online courses** from platforms like **Udemy**, **edX**, and **Coursera**. It allows users to filter and browse curated courses by category, rating, level, and more — all in a responsive, visually appealing interface.
---

## 🚀 Features

- 🎯 Intelligent course filtering by:
  - Category
  - Level (Beginner, Intermediate, Advanced)
  - Minimum Rating
- 💻 Responsive and modern UI/UX design
- 📊 Data merged from multiple platforms (Udemy, edX, Coursera)
- 🔍 Real-time filtering without needing a database
- 🖼️ Attractive About page with detailed visuals and layout
- 🌍 Fully responsive for both desktop and mobile screens

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Data Handling:** Pandas
- **Templates:** Jinja2
- **Course Data:** Excel files (`Udemy1.xlsx`, `Edx.xlsx`, `Coursera.xlsx`)

---

## 📁 Project Structure

```
SkillSphere/
├── static/
│   ├── style.css
│   ├── image.png
│   └── about.png
│   |── step1.png
│   └── step2.png
│   └── step3.png
├── templates/
│   ├── index.html
│   └── about.html
├── Udemy1.xlsx
├── Edx.xlsx
├── Coursera.xlsx
├── app.py
```

---

## ⚙️ Installation & Running Locally

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/skillsphere.git
cd skillsphere
```

2. **Create a virtual environment & activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app:**

```bash
python app.py
```

## 📌 To-Do / Future Features

- ✅ Add course sorting (by rating, price)
- ⏳ Add login/authentication for personalized bookmarks
- ⏳ Connect to live APIs (future integration with platform APIs)
- ⏳ Add course thumbnails for visual appeal
