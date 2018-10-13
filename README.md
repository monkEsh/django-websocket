# django-websocket

Simple application to display user login status using websockets

Refered from : https://realpython.com/getting-started-with-django-channels/

**Pre requisites**
1. Redis server on localhost or configure remote server in settings.py

**Steps to run app**
1. Clone code : https://github.com/monkEsh/django-websocket.git
    ```bash
    # git clone https://github.com/monkEsh/django-websocket.git
    ```
2. Goto django-websocket dir and install requirements.txt
    ```bash
    # virtualenv -p python3.6 venv
    # pip install requirements.txt
    ```
3. Goto project dir
    ```bash
    # cd example_channels/
    ```
3. Create migrations and migrate models
    ```bash
    # python manage.py makemigrations
    # python manage.py migrate
    ```
4. Start application
    ```bash
    # python manage.py runserver
    ```
**Sanity check**
1. Create user : 
    ```bash
    127.0.0.1:8000/ws/sign_up
    ```
2. Login user
    ```bash
    127.0.0.1:8000/ws/log_in
    ```
3. Logout user
    ```bash
    127.0.0.1:8000/ws/log_out
    ```
4. Check user status
   ```bash
    127.0.0.1:8000/
    ```
