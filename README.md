# 🧑‍🎓 Student Result Management System

A Django-based web application that allows students to securely check their exam performance using their unique roll numbers.
The system ensures only authenticated users can access personal academic results, including biodata, subject-wise marks,
percentage, and pass/fail status.

https://github.com/user-attachments/assets/77415bec-6f14-4b49-8a31-9fb38739dc18

---

## 🚀 Features

- 🔐 **User Authentication** — Secure login required to view student results  
- 🎯 **Result Lookup by Roll Number** — Each student can search using their assigned roll number (1–2000)  
- 📊 **Detailed Report View** — Displays:
  - Student biodata
  - Subject-wise marks
  - Overall percentage
  - Pass/Fail status  
- 🛠️ **Admin Panel** — Admins can add, update, and manage results from Django's built-in admin interface

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Database:** MySQL  
- **Frontend:** HTML, CSS (Django templates)  
- **Authentication:** Django's default auth system  
- **Version Control:** Git, GitHub  

---
```markdown
## 📂 Project Structure

student_perfomance
├── view_result/                 # Main app for handling results
│   ├── models.py                # Database models for student and result
│   ├── views.py                 # Views for handling result lookup
│   ├── urls.py                  # URL routing for the results app
├── templates/                   # HTML templates
├── student_perfomance/          # Project configuration
│   └── settings.py              # Project settings
├── MySQL                        # Database
└── manage.py                    # Django management script

````

---

## 🚦 How to Run the Project Locally

1. **Clone the repository**
```bash
git clone https://github.com/m-mahmood/students_performance_check
cd student_perfomance
````

2. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations and run the server**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. **Access the app**

* Visit `http://127.0.0.1:8000/`
* Use the Django admin panel at `/admin/` to add student results

---

## 👨‍💻 Admin Credentials (for testing)

> ⚠️ Make sure to change default credentials in production!

```bash
python manage.py createsuperuser
```

Then enter your email/username/password as prompted.

---

## 📌 Future Improvements

* Add pagination and search filters
* Export results as PDF
* Role-based permissions (e.g., teachers, principals)
* Responsive frontend using Bootstrap or Tailwind CSS

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📄 License

Copyright (c) 2025 M Mahmood

All rights reserved.

This software and associated documentation files (the "Software") are the exclusive property of the author.

Unauthorized copying, use, modification, distribution, or any form of reuse of this code, in whole or in part, is strictly prohibited.

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, or noninfringement. 
In no event shall the author be liable for any claim, damages, or other liability arising from the use of this Software.

For inquiries about licensing, please contact the author directly.

---

## 🙋‍♂️ Author

**Muhammad Mahmood**

* 💼 Meta Certified Backend Developer
* 🌐 [LinkedIn](https://www.linkedin.com/in/mahmoodweb/)
* 🔗 [GitHub](https://github.com/m-mahmood)


