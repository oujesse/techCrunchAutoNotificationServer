# TechCrunch Auto Notification
This project creates a web server where users can enter keywords and the server will automatically notify 
them if any keywords show up in a new TechCrunch article. 

Note: Server hosting only compatible with Linux OS

## Setup
1. Clone the repository.

2. Install python 3 and pip3 along with psycopg2 2.77, suffix-tree, django-webpush, django-crontab,
ngrok, and postgresql
    ```bash
    $ sudo apt install python3.6 python3-pip
    $ pip3 install psycopg2 suffix-trees django-webpush postgresql django-crontab
    $ wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    $ unzip ngrok-stable-linux-amd64.zip
    $ sudo mv ngrok /usr/local/bin
    ```
8. Setup Postgresql with your desired database name along with admin username and password
    ```bash
    $ sudo su - postgres
    $ psql
    $ CREATE DATABASE database_name;
    $ CREATE USER desired_username WITH PASSWORD 'desired_password';
    $ GRANT ALL PRIVILEGES ON DATABASE database_name TO desired_username;
    $ \q
    $ exit
    ```
9. Enter the techCrunchAutoNotification directory you cloned in step 1
10. Open up and edit the settings.py file found in techCrunchAutoNotification/mysite/mysite/ and then 
edit DATABASES such that it looks like this (make sure the database_name, desired_username, and desired_password
all match the information you entered during step 9): 
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'desired_username',
        'PASSWORD': 'desired_password',
        'HOST': 'localhost',
        'PORT': '',
        }
    }
    ``` 
11. Enter the techCrunchAutoNotification/mysite/ directory and run sync up the database with the 
models in the project
    ```bash
    $ python3 manage.py makemigrations newsNotification
    $ python3 manage.py migrate --run-syncdb
    $ python3 manage.py migrate
    ```
13. Activate the crontab tasks
    ```bash
    python3 manage.py crontab add
    ```
14. Click this link [here](https://web-push-codelab.glitch.me/), and then inside the settings.py from step
10, enter the Vapid public and private keys you received from the link into WEBPUSH_SETTINGS along with
an email you wish to receive server error notifications from:
    ```
    WEBPUSH_SETTINGS = {
        "VAPID_PUBLIC_KEY": "Vapid Public Key",
        "VAPID_PRIVATE_KEY":"Vapid Private Key",
        "VAPID_ADMIN_EMAIL": "admin@example.com"
    }
    ```
15. Next look up your local IP [here](https://www.whatismyip.com/) and inside settings.py, enter that ip using quotes into ALLOWED_HOSTS:
    ```
    ALLOWED_HOSTS = ['your_local_ip']
    ```
16. Now run your server using your local IP from the techCrunchAutoNotification/mysite/ directory
    ```
    python3 manage.py runserver your_ip:8000
    ```
18. Now activate ngrok
    ```
    ngrok http your_ip:8000
    ```
19. In the window that ngrok opens, you will see a url to the right of the second "Forwarding". Copy
that url and paste it into ALLOWED_HOSTS from step 15 (make sure you don't paste "https://"):
    ```
    ALLOWED_HOSTS = ['your_local_ip', 'ngrok_url']
    ```
20. Go to the bottom of the file and change LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL to 
https://ngrok_url/newsNotification/ using the ngrok_url from step 19:
    ```
    LOGIN_REDIRECT_URL = 'https://ngrok_url/newsNotification/'
    LOGOUT_REDIRECT_URL = 'https://ngrok_url/newsNotification/'
    ```
21. Now using that ngrok url, go to https://ngrok_url/newsNotification to visit your working server! 
Create an account, login, enter your desired keywords, and click the "subscribe to notifications" to 
be notified of when TechCrunch adds an article related to one of your keywords. 


Warning: This project is still in the experimental phase, and I will not be held responsible for security vulnerabilities. 
