# Social Network REST API

# Overview:-
    This is a social network REST API built with Django and Django REST Framework. The application supports user signup, login, friend requests, and more.

# Installation

1. Clone the repository:-
git clone <repository-url>

2. Navigate to the project directory:-
cd socialnetwork

3. Install dependencies:-
pip install -r requirements.txt

4. Set up the database in settings.py file:-

Add Your database details:-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'social_network',
        'USER': 'Add Your User Here',
        'PASSWORD': 'Add Your Password Here',
        'HOST': 'Add Your host Here',
        'PORT': Add Your Port Here,
    }
}

Then run migrate:-  python manage.py migrate


5. Use this command for Create a superuser for admin page:-

python manage.py createsuperuser


# Running the Development Server:-

Start the development server by running:-
python manage.py runserver

The server will start running at http://localhost:8000/.

Admin page: http://127.0.0.1:8000/admin/


# Token Generation:- 
This API is secured by token-based authentication. To access it:
    1. Generate a token in the admin page by logging in.
    2. Include the token in the request header when making requests to the API. Use the Authorization header prefixed with the string "Token".
    Example: headers = {'Authorization': 'Token your_token_here'} in Postman or Thunder Client.


# API Endpoints:- 
Use token to access APIs.


# Features

`api/signup/`: User Registration
`api/login/`: User Authentication
`api/search/`: Search for Users
`api/friend-request/`: Send and Manage Friend Requests
`api/friends/`: Friend list view
`api/pending-requests/`: pending Friend list view


# Prerequisites

- Python 3.10
- Docker (optional, for containerization)

# To create and share a Postman collection for your API endpoints, follow these steps:

1. Create a Postman Collection:

- Open Postman.
- Click on "New Collection" in the top left.
- Name your collection, for example, "Social Network API".

2. Add Requests to Your Collection:

- For each API endpoint, create a new request.
- Set the request type (GET, POST, PUT, etc.) and the URL for each endpoint.
- Add any necessary headers (e.g., Content-Type: application/json, Authorization: Token <your_token>).
- Add the request body if needed (for POST and PUT requests)

# Running the Test Suite:- 

Execute the following command in your terminal for test suite run:- 
python manage.py test

All the tests defined in the tests.py file and display the results.