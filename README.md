# Blog Post Application

![License](https://img.shields.io/github/license/M-Tayyab06/Blog_Post_Application?color=blue)
![Stars](https://img.shields.io/github/stars/M-Tayyab06/Blog_Post_Application?style=social)
![Issues](https://img.shields.io/github/issues/M-Tayyab06/Blog_Post_Application)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Blog](https://img.shields.io/badge/Blog_App-Node.js-blue?logo=node.js)

# 📝 Django Blogging Application

A **simple, elegant, and responsive** blogging platform built with **Django**, featuring a sleek **dark-themed UI** powered by **Tailwind CSS**. Users can create, view, and delete blog posts with optional image uploads. Includes a powerful Django Admin interface for post management.

---

## ✨ Features

- **🔊 Create Posts** – Add new blog entries with a title, content, and optional image upload.
- **📄 View Posts** – Display posts in a clean, card-based layout with side-by-side image and content.
- **❌ Delete Posts** – Remove posts easily with a confirmation prompt.
- **🛠 Admin Interface** – Full CRUD access via Django’s admin panel.
- **📱 Responsive Design** – Tailwind CSS ensures a consistent look across all screen sizes.

---

## 💠 Technologies Used

- **Python 3.9+** – Core programming language.
- **Django 4.2** – High-level web framework for building scalable apps.
- **SQLite** – Lightweight default database (easily swappable with MySQL/PostgreSQL).
- **Tailwind CSS** – Utility-first CSS framework for beautiful, dark-themed styling.
- **Pillow** – Image handling and upload support.

---

## 🛆 Prerequisites

- Python 3.9 or higher
- Git
- A modern web browser

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 6. Create Media Directory

```bash
mkdir -p media/post_images
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to start blogging!

---

## 🧑‍💻 Usage

- **Create a Post:** Navigate to the homepage → click “Create a New Post” → fill in the form → click “Post”.
- **View Posts:** Scroll through the homepage to see all blog entries in a responsive, card-based layout.
- **Delete a Post:** Click “Delete” on a post card and confirm.
- **Admin Panel:** Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials to manage all posts.

---

## 📁 Project Structure

```
blog_project/
├── blog_app/               # Core app: models, views, templates
├── blog_project/           # Django project configuration
├── media/post_images/      # Uploaded blog images
├── db.sqlite3              # SQLite database file
├── manage.py               # Django CLI management
└── requirements.txt        # Python dependencies
```

---

## 🌆 Screenshots
![image](https://github.com/user-attachments/assets/06e8882a-c66b-4b5f-be4b-b53f9c92c893)


---

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, create a new branch for your feature or fix, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

