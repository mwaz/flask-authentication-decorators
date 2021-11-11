# Authentication Decorators in Flask

[![CircleCI](https://circleci.com/gh/mwaz/flask-authentication-decorators.svg?style=svg)](https://circleci.com/gh/mwaz/flask-authentication-decorators)

<p align="center"><img src="https://avatars3.githubusercontent.com/u/59034516"></p>


An API designed in flask. Uses CircleCI as the CI/CD tool and pyjwt handles the authentication. The API allows users to add and manage books in a library. Users get auth token after login which can then be used to access othr routes and perform other actions.

## Setup
1. Create directory and `cd` into the directory
2. clone the repo `git clone https://github.com/mwaz/flask-authentication-decorators.git`
3. setup a virtualenv `pipenv shell`
4. install dependencies `pipenv install`

## Running the application
> type: `python run.py`
> serving on: `https://127.0.0.1:5000/`

## Running the tests
> type: `pipenv run pytest`

## Endpoints
- Use postman or curl to test the endpoints
- Parse auth token in `x-access-token` header.
1. User register: POST `/signup`
2. User login: POST `/login`
3. Create a book: POST `/bookapi/addbook`
4. Pull all available books: GET `/bookapi/books`
5. Remove book DELETE `/bookapi/book/<book_id>`


## Details

This repo is built following a tutorial published on CircleCI blog under the CircleCI Guest Writer Program.

- Blog post: [Authentication Decorators in Flask][blog]
- Author's GitHub profile: [Waweru Mwaura][author]

### About CircleCI Guest Writer Program

Join a team of freelance writers and write about your favorite technology topics for the CircleCI blog. Read more about the program [here][gwp-program].

Reviewers: [Ron Powell][ron], [Stanley Ndagi][stan]


[blog]: https://circleci.com/blog/authentication-decorators-in-flask/
[author]: https://github.com/mwaz

[gwp-program]: https://circle.ci/3ahQxfu
[ron]: https://github.com/ronpowelljr
[stan]: https://github.com/NdagiStanley
