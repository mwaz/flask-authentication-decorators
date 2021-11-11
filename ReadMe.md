# Flask-library-API
An API designed in flask. Uses CircleCI as the CI/CD tool and pyjwt handles the authentication

## About
A library management API, allows users to add and manage books in a library.
- Users get auth token after login
## Setup
1. Create directory and `cd` into the directory
2. clone the repo `https://github.com/mwaz/authentication-decorators-flask.git`
3. setup a virtualenv `pipenv shell`
4. install dependencies `pipenv install`

### Running
> type: `python run.py`
> serving on: `https://127.0.0.1:5000/`

## Endpoints
- Use postman or curl to test the endpoints
- Parse auth token in `x-access-token` header.
1. User register: POST `/signup`
2. User login: POST `/login`
3. Create a book: POST `/bookapi/addbook`
4. Pull all available books: GET `/bookapi/books`
5. Remove book DELETE `/bookapi/book/<book_id>`