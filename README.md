# api_twt

This project is a comprehensive API developed using Django Rest Framework, designed to serve as the backbone for the front-end project located at [like-twitter](https://github.com/IsacJfs/like-twitter). It aims to provide a robust, scalable, and efficient backend structure, ensuring seamless integration and functionality for the front-end application.

## Key Features:

- **Django Rest Framework**: Utilizes the powerful and flexible Django Rest Framework to create API endpoints that are both efficient and easy to maintain.
- **Seamless Integration**: Specifically tailored to complement and enhance the functionality of the [like-twitter](https://github.com/IsacJfs/like-twitter) front-end project.
- **Scalable Architecture**: Designed with scalability in mind, allowing for future expansions and modifications as the front-end project evolves.
- **Security and Performance**: Prioritizes security and performance, ensuring that data handling is both safe and efficient.

## Objective:

The primary objective of this backend API project is to provide a solid and reliable infrastructure that supports the various features and functionalities of the 'like-twitter' front-end. By focusing on seamless data flow and robust service architecture, this project aims to elevate the user experience and overall performance of the front-end application.

For more detailed information about the API endpoints, data structures, and usage, please refer to the sections below.

---

This enhanced description provides a clearer understanding of the project's purpose, its relation to the front-end project, and its core features. It's important that the README is inviting and informative, as it's often the first point of contact for potential users and contributors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project environment:

1. **Create a Virtual Environment:**
   ```
   python -m venv env
   ```

2. **Activate the Virtual Environment:**

   - On Windows:
     ```
     .\env\Scripts\activate
     ```

   - On Linux or macOS:
     ```
     source env/bin/activate
     ```

3. **Install Dependencies:**

   Install the required packages using the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add the Django secret key:
   ```
   DJANGO_SECRET_KEY='your_secret_key'
   ```

5. **Start the Server:**

   Run the following command in the root directory to start the server:
   ```
   python manage.py runserver
   ```

## Usage

This project uses the Djoser library for authentication and user management. Refer to the [Djoser Documentation](https://djoser.readthedocs.io/en/latest/getting_started.html) for detailed information. Below are the standard endpoints provided by Djoser:

- **User Management Endpoints:**
  - Create User: `/auth/users/`
  - Get User: `/auth/users/me/`
  - Confirm User: `/auth/users/confirm/`
  - Resend Activation Email: `/auth/users/resend_activation/`
  - Set Password: `/auth/users/set_password/`
  - Reset Password: `/auth/users/reset_password/`
  - Reset Password Confirmation: `/auth/users/reset_password_confirm/`
  - Set Username: `/auth/users/set_username/`
  - Reset Username: `/auth/users/reset_username/`
  - Reset Username Confirmation: `/auth/users/reset_username_confirm/`

- **Token Management Endpoints:**
  - Token Login: `/auth/token/login/`
  - Token Logout: `/auth/token/logout/`
