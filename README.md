Django Blogging Application
A simple and elegant blogging application built with Django, allowing users to create, view, and delete blog posts with optional images. The app features a modern, dark-themed interface styled with Tailwind CSS and includes an admin panel for managing posts.
Features

Create Posts: Add blog posts with a title, content, and an optional image.
View Posts: Display all posts in a visually appealing card layout, with images and content side-by-side.
Delete Posts: Easily delete posts with a confirmation prompt.
Admin Interface: Manage posts (view, edit, delete, or add) via the Django admin panel.
Responsive Design: Styled with Tailwind CSS for a modern, dark-themed UI that works on all devices.

Technologies Used

Python 3.9+: Core programming language.
Django 4.2: Web framework for building the application.
SQLite: Lightweight database for development (can be switched to MySQL or PostgreSQL for production).
Tailwind CSS: Utility-first CSS framework for styling.
Pillow: Python library for handling image uploads.

Prerequisites

Python 3.9 or higher installed on your system.
Git for cloning the repository.
A web browser to access the app.

Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

4. Set Up the Database
Run migrations to set up the SQLite database:
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional)
Create a superuser to access the admin interface:
python manage.py createsuperuser

Follow the prompts to set a username, email, and password.
6. Create Media Directory
Create a directory to store uploaded images:
mkdir -p media/post_images

7. Run the Development Server
Start the Django development server:
python manage.py runserver

The app will be available at http://127.0.0.1:8000/.
Usage

Create a Post:
Visit http://127.0.0.1:8000/.
Click "Create a New Post".
Fill in the title, content, and optionally upload an image.
Click "Post" to publish.


View Posts:
All posts are displayed on the homepage in a card layout.


Delete a Post:
Click the "Delete" button on a post card and confirm the action.


Admin Interface:
Access the admin panel at http://127.0.0.1:8000/admin/.
Log in with your superuser credentials.
Manage posts (view, edit, delete, or add new ones).



Project Structure

blog_app/: Contains the main app logic (models, views, templates, etc.).
blog_project/: Django project settings and configuration.
media/post_images/: Stores uploaded images.
db.sqlite3: SQLite database file.
manage.py: Django management script.
requirements.txt: List of Python dependencies.

Screenshots
Homepage displaying blog posts with a modern, dark-themed UI.
Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
