# Django REST Framework JWT Example
Creating a Django Project with JWT Auth and Middleware


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/ravidtu/goGlocal.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```
```bash
Login to admin-> **127.0.0.1:8000/admin/**
```
create new user 
API Documentation :==
```bash
**https://documenter.getpostman.com/view/2964291/2s9Y5VUjEg**
```

The API endpoints will be available at
```bash
 **127.0.0.1:8000/api/user/login/**.
 ```
 
  With Post method
  ```bash
Payload:-
{
    "username":"ravi@gmail.com",
    "password":"qwerty@123"
}
```
Hit endpoints **127.0.0.1:8000//api/user/profile/** with GET method

