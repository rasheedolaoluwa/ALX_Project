# ALX_Project - Project Ranora

## Introduction

Welcome to my ALX_Project, a comprehensive web application designed to provide tailored financial recommendations based on user risk profiles and preferences. Our goal is to empower users to make informed investment decisions that align with their financial goals and risk tolerance.

### Links
- **[Deployed Site](http://rasheeed.tech/)**
- **[Final Project Blog Article](#)**
- **Authors:**
  - [LinkedIn](https://www.linkedin.com/in/radeyola) - Rasheed Olaoluwa

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rasheedolaoluwa/ALX_Project.git
   cd ALX_Project

2. **Clone the Repository:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Set Up Environment Variables:**
   ```bash
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=postgresql://yourusername:yourpassword@localhost:5432/yourdatabase
   MAIL_USERNAME=your_email@example.com
   MAIL_PASSWORD=your_email_password
   SECURITY_PASSWORD_SALT=your_security_salt
   
4. **Initialize the Database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

5. **Run the Application:**
   ```bash
   flask run


## Usage

To use the ALX_Project, navigate to the deployed site [here](http://rasheeed.tech/). You can register an account, log in, and explore the financial recommendations tailored to your profile. The application features user authentication, personalized dashboards, and detailed investment recommendations.

### Screenshots
[Homepage](https://imgur.com/a/B4D9DIA/800x400?text=Homepage+Screenshot)
[Dashboard](https://imgur.com/MRC5Suk/800x400?text=Dashboard+Screenshot)
[Profile Setup](https://imgur.com/xezYD7c/800x400?text=Profile+Setup+Screenshot)

## Contributing

We welcome contributions to the ALX_Project! If you are interested in contributing, please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch:**
   ```bash
   git checkout -b feature-branch
3. **Commit Your Changes:**
   ```bash
   git commit -m "Add some feature
4. **Push to the Branch:**
   ```bash
   git push origin feature-branch
5. **Open a Pull Request**

## Related Projects
N/A

## Licensing
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.

## Project Background

### Inspiration

The inspiration for ALX_Project came from a desire to simplify financial planning and investment decision-making for individuals. We noticed that many people struggle to find personalized financial advice that takes into account their unique risk tolerance and financial goals. Our project aims to fill this gap by providing a user-friendly platform that delivers tailored financial recommendations.

### Challenges

Throughout the development of ALX_Project, we faced several challenges:
- **Database Integration:** Ensuring seamless integration with PostgreSQL for robust data handling.
- **User Authentication:** Implementing secure and efficient user authentication mechanisms.
- **Data Privacy:** Ensuring user data is handled with the utmost confidentiality and security.

### Future Vision

In the next iteration, we envision adding the following features:
- **Real-Time Market Data:** Integration with financial APIs to provide real-time market data and trends.
- **Advanced Analytics:** Enhanced analytics tools to help users better understand their investment performance.
- **Mobile Application:** Developing a mobile version of the application to make financial planning accessible on the go.

### Technical Details

Our application leverages the following technologies:
- **Flask:** A lightweight WSGI web application framework.
- **SQLAlchemy:** SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL:** A powerful, open source object-relational database system.
- **Flask-Mail:** A Flask extension for sending emails.
- **Gunicorn:** A Python WSGI HTTP Server for UNIX.

### Screenshots and Visuals

We believe in the power of visuals to tell our story. Here are some screenshots from our application to give you a glimpse of what we have built:
![Home Page](https://github.com/rasheedolaoluwa/ALX_Project/assets/102518368/1eedaaa9-6b3e-411b-a28d-415bd5ea1ff9)
![Dashboard](https://github.com/rasheedolaoluwa/ALX_Project/assets/102518368/cddf7dbc-af78-4ee2-b45c-ab5a7dd9e4f9)
![Profile Set up](https://github.com/rasheedolaoluwa/ALX_Project/assets/102518368/60e7db2e-f848-4c2e-acbc-dd96201683d1)  
