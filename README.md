# System Admin GUI
It contains the assigments from 3 till 7.

### Installation (python 2.7 recommended)

- Get the requirements

    `$ sudo apt-get install python-pip`

- Fork and clone the system-admin-gui repository

	`$ git clone https://github.com/<Username>/system-admin-gui`

- cd into `project`

	`$ cd system-admin-gui`

- Install requirements from `requirements.txt`

    `$ pip install -r requirements.txt`

- Apply the migrations(Already included for ease)

	`python manage.py makemigrations`

	`python manage.py migrate`

- Now run the server

	`$ python manage.py runserver`

open [127.0.0.1:8000](127.0.0.1:8000) in the browser

- Create the admin

	`python manage.py createsuperuser`

- Add the relevant information

- open [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
