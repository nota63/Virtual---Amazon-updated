# Virtual Amazon

Virtual Amazon is a web application built using Django that provides an e-commerce platform for various products like books, mobiles, clothes, laptops, electronics, and more. It includes functionalities for user and admin logins, product browsing, feedback, and more.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User and Admin login functionality
- Product browsing for various categories including books, mobiles, clothes, laptops, and electronics
- Feedback submission via WhatsApp integration
- Admin functionalities for managing credentials and queries
- Voice feedback using `pyttsx3`

## Installation

### Prerequisites
- Python 3.6+
- Django 3.x+
- `pywhatkit` for WhatsApp integration
- `pyttsx3` for text-to-speech functionality

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/virtual-amazon.git
    cd virtual-amazon
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

### User Login
- Users can log in through the user login page and access various product categories.

### Admin Login
- Admins can log in through the admin login page and manage the platform, view feedback, and respond to queries.

### Product Browsing
- Browse different product categories including books, mobiles, clothes, laptops, electronics, and more.

### Feedback Submission
- Users can submit feedback, which is sent directly to the developer's WhatsApp using `pywhatkit`.

## Project Structure
virtual-amazon/
├── virtual_amazon/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
├── templates/
│ ├── owner_admin.html
│ ├── home.html
│ ├── about-us.html
│ ├── ebook.html
│ ├── mobile.html
│ ├── clothes.html
│ ├── laptops.html
│ ├── electronics.html
│ ├── shoes.html
│ ├── antivirus.html
│ ├── watches.html
│ ├── monitors.html
│ ├── arduino.html
│ ├── televisions.html
│ ├── mouse.html
│ ├── games.html
│ ├── hash1290.html
│ ├── help.html
│ ├── developer.html
│ ├── feedback.html
│ ├── amazon.html
│ ├── flipkart2.html
│ ├── documentation.html
│ ├── myntra.html
│ ├── collaboration.html
│ ├── about_web.html
│ ├── update.html
│ ├── car.html
│ ├── bike.html
│ ├── footer.html
│ ├── choice_login.html
│ ├── power_off.html
│ ├── user_login.html
│ ├── admin_login.html
│ ├── admin_home.html
│ ├── admin_credentials.html
│ ├── admin_help.html
├── book/
├── mobile/
├── clothes/
├── laptops/
├── electronics/
├── shoes/
├── antivirus/
├── watches/
├── monitors/
├── arduino/
├── televisions/
├── mouse/
├── games/
├── amazon2/
├── flipkart2/
├── myntra/
├── car/
├── bike/
├── manage.py


## Contributing
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
