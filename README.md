🥊 Boxing Attendance Tracker 🥊
A Django-powered web app for managing boxers and tracking their attendance.

💡 Features
✅ Add and manage boxers

✅ Mark attendance with options: Present / Absent / Excused

✅ View individual boxer reports

✅ Filter attendance by date

✅ Summarized attendance overview with percentages

✅ Admin panel to manage everything

✅ Responsive design (mobile-friendly)

✅ Local deployment with optional Ngrok support for remote access

📦 Tech Stack
Backend: Django 5.x

Frontend: HTML, CSS (custom + static files)

Database: SQLite (default)

Deployment: Localhost, Ngrok, or any WSGI-compatible server

## 🛠 Tech Stack

- **Backend:** Django 5.x  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **Deployment:** Localhost or via Ngrok (optional)

---

## 🚀 Getting Started

1. Clone the repository
```bash
git clone https://github.com/your-username/boxing-attendance-tracker.git
cd boxing-attendance-tracker

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations and run the development server
python manage.py migrate
python manage.py runserver

5. Access the app
Open in your browser:
http://127.0.0.1:8000/attendance/mark/

