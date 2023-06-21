# Zap-Buy Django Project

Welcome to the Zap-Buy Django project! This project utilizes custom user authentication and aims to incorporate dynamic routes. This README.md file will guide you through the project setup and provide information on how to contribute to the repository.

## Project Description

Zap-Buy is a Django-based web application designed to facilitate online shopping. The project implements custom user functionality, allowing users to create accounts, log in, and perform various actions within the application.

The project also focuses on dynamic routes, enabling users to navigate through different pages and perform specific actions based on the route. This feature enhances the overall user experience and provides a more interactive and seamless shopping experience.

## Installation

To get started with the Zap-Buy Django project, follow the steps below:

1. Clone the repository:

`git clone https://github.com/anirban-1009/Zap-Buy.git`


2. Change into the project directory:

`cd Zap-Buy`


3. Create a virtual environment:

`python3 -m venv env`


4. Activate the virtual environment:

On macOS and Linux

`source env/bin/activate`
On Windows

`env\Scripts\activate`


5. Install project dependencies:

`pip install -r requirements.txt`


6. Run database migrations:

`python manage.py migrate`


7. Start the development server:

`python manage.py runserver`


8. Open your web browser and visit http://localhost:8000 to access the application.

## Contribution Guidelines

We welcome contributions to the Zap-Buy project! If you would like to contribute, please follow these guidelines:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name for your feature or bug fix:

`git checkout -b <branch_name>`


3. Make your modifications and ensure that the code follows the project's coding style.

4. Write tests to cover any new functionality or changes you have made.

5. Run the project's tests to ensure they pass:

`python manage.py test`


6. Commit your changes and provide a meaningful commit message:

`git commit -m "Your commit message"`


7. Push your branch to your forked repository:

`git push origin <branch_name>`


8. Open a pull request on the main repository, describing the changes you have made.

9. Wait for the maintainers to review your pull request and address any feedback or suggestions.

Thank you for considering contributing to the Zap-Buy project. Your contributions are greatly appreciated!

## License

The Zap-Buy Django project is licensed under the [GNU General Public License (GPL)](LICENSE.md).
