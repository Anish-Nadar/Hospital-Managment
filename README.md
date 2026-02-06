# 🏥 Hospital Management System

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](https://github.com/Anish-Nadar/Hospital-Managment/blob/main/CONTRIBUTING.md)

A Django-based web application for managing hospital operations, including patient registration, doctor management, appointments, and contact forms.

## ✨ Features

- 🩺 **Patient Management**: Register patients, manage profiles, and handle logins.
- 👨‍⚕️ **Doctor Management**: View doctor profiles with images and specialties.
- 📅 **Appointment Booking**: Patients can book appointments with doctors.
- 📧 **Contact Forms**: Submit inquiries or feedback.
- 🔧 **Admin Panel**: Django admin interface for managing data.
- 🎨 **Responsive Design**: Basic styling with CSS.

## Installation

### Prerequisites
- 🐍 Python 3.10–3.12 (recommended: 3.12)
- 📚 Git

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anish-Nadar/Hospital-Managment.git
   cd Hospital-Managment
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install django pillow
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **(Optional) Create a superuser for admin access**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/` (use superuser credentials)

## Usage

- **Home Page**: Overview of the hospital and navigation.
- **Register/Login**: Patients can register and log in.
- **Doctors List**: View available doctors.
- **Book Appointment**: Logged-in patients can book appointments.
- **Contact**: Submit contact forms.

## Project Structure

```
Hospital-Managment/
├── hospitalapp/          # Main Django app
│   ├── models.py         # Database models (Patient, Doctor, etc.)
│   ├── views.py          # View functions
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, images
│   └── migrations/       # Database migrations
├── hospmgmt/             # Django project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── media/                # Uploaded files (e.g., doctor images)
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── README.md             # This file
```

## Technologies Used

- **Backend**: Django (Python web framework)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS (basic styling)
- **Image Handling**: Pillow (for ImageField)

## Contributing

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on GitHub or contact the repository owner.