# Doctors Hub Application

The Doctors Hub Application is a comprehensive web application designed to facilitate the search and discovery of doctors. This project, built with Django, HTML, CSS, and Python, features a user-friendly interface with essential functionalities to enhance user experience.
## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Code Overview](#code-overview)
  - [Models](#models)
  - [Views](#views)
  - [Templates](#templates)
  - [Static Files](#static-files)
- [Customization](#customization)
- [License](#license)

## Project Structure

```plaintext
clinic_management_system/
│
├── clinic_website/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── registration/register.html
│   │   ├── registration/login/html
│   │   ├── base.html
│   │   ├── doctor_details.html
│   │   ├── home.html
│   │   ├── index.html
│   │   └── search_results.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── clinic/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Features

- **User Registration & Authentication:** Patients and doctors can register and log in.
- **Doctor Search:** Users can search for doctors by specialization and area.
- **Doctor Profiles:** Detailed profiles of doctors including their contact information.
- **Responsive Design:** The application is fully responsive and mobile-friendly.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/itsyaya/clinic.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd clinic
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Visit the landing page:**
   Navigate to `http://127.0.0.1:8000/` in your web browser.
2. **Register or Login:**
   Use the registration page to create a new account or log in with an existing account.
3. **Search for Doctors:**
   Use the search functionality to find doctors by specialization and area.
4. **View Doctor Details:**
   Click on a doctor’s name to view their detailed profile.

## Technologies Used

- **Backend:** Django, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Styling:** Mulish Font, Custom CSS

## Code Overview

### Models

- **User:** Extends the default Django `User` model to include additional fields relevant to the clinic's context.
- **Doctor:** Stores details about the doctors including name, phone, and address.
- **Appointment:** Manages appointments booked by patients.

### Views

- **Home View:** Displays the landing page with search functionality.
- **Doctor Detail View:** Renders detailed information about a selected doctor.
- **Register & Login Views:** Handles user authentication and registration.

### Templates

- **base.html:** The main template that includes the navigation menu and links to CSS and JS files.
- **login.html & register.html:** Handles user authentication with forms for login and registration.
- **landing.html:** The landing page where users can search for doctors.
- **doctor_details.html:** Displays detailed information about a selected doctor.

### Static Files

- **CSS:** Custom styles for the application.
- **JS:** Handles dynamic aspects of the UI.
- **Images:** Contains images used across the site.

## Customization

- **Theme Colors:** The primary color used is blue (#458ff6). You can update this in the CSS files located in `static/css/`.
- **Font:** The application uses the Mulish font. You can change the font by modifying the link in the `<head>` section of `base.html`.
- **Templates:** Modify the templates in the `templates/` directory to customize the layout and design.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This template can be adapted based on your specific project requirements and any additional features or customizations you have made.
