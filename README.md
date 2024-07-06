Notes
Notes is a simple and intuitive web application designed to help users manage their notes effectively. With Notes, you can create, view, and delete notes with ease. Each note can be categorized by priority, making it easy to organize and find important information quickly. Built using Django and Bootstrap, Notes offers a responsive and user-friendly interface.

Key Features:
Create Notes: Easily add new notes with a title, content, and priority level (Low, Medium, High).
View Notes: Browse through all your notes on the main page.
Delete Notes: Remove notes that are no longer needed with a single click.
Prioritization: Categorize notes based on their priority to manage your tasks better.
Technologies Used:
Backend: Django
Frontend: Bootstrap, HTML, CSS
Database: SQLite (default for Django)
How to Clone the Project to Your Computer
Follow these steps to clone and set up the "Notes" project from GitHub:

Clone the Repository

Open your terminal and execute the following command to clone the repository:

git clone https://github.com/ftox121/Note.git

cd Note
python3 -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000 to view the application
