# classcodeshare
ClassCodeShare

📖 Project Overview

ClassCodeShare is a classroom engagement app that allows a host (lecturer/tutor) to create live coding sessions where guests (students) can submit code snippets in response to tasks. Lecturers/tutors emphasize student engagement in class during coding classes but unfortunately not all students have access to laptops/PCs. This application enables them to answer coding questions and engage using any device they have as long as there's internet connection.

- Location-based participation ensures only students near the host can join.
- Students can write and run code via an external code execution API.
- Hosts can store session history, tasks, and student submissions for grading or future review.


✨ Features

- User Roles: Host (educator) & Guest (student).

- Session Management: Hosts can create/join/close live sessions.

- Tasks: Hosts assign coding tasks with optional deadlines.

- Code Submissions: Students submit code snippets per task.

- Location Capture: Ensures engagement from nearby learners.

- Session History: Hosts may choose to keep logs of tasks & submissions.

- Activity Log: Tracks important actions (session joined, task submitted, etc.).

- External Code Execution API (optional): Run snippets inside the app.


🛠 Tech Stack

- Backend Framework: Django + Django REST Framework

- Database: SQLite (for development) → PostgreSQL (for production/Heroku)

- Deployment: Heroku


🗄 Database Models

- UserProfile → extends Django’s User with role (host/guest).

- Session → created by a host, students join.

- Task → belongs to a session, includes description + optional deadline.

- Submission → student submits a code snippet for a task.

- ActivityLog → records actions like joining a session or submitting a task.


🚀 Getting Started

Prerequisites

- Python 3.x

- Django & Django REST Framework installed

Setup
#
git clone <repository_url>
cd codeshare
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
#

Access admin panel at: http://127.0.0.1:8000/admin/