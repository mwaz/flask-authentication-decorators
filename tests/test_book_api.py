"""Tests for User Authentication"""
import unittest
import json
import ast

from werkzeug.wrappers.response import Response
from library.main import app, db
from config import app_config

def getLoginToken(self):
        """"Method to get a login token
        """
        user_register = self.client().post('/signup', data=self.user_details, content_type="application/json")
        self.assertEqual(user_register.status_code, 201)
        user_login = self.client().post('/login', data=self.user_details, content_type="application/json")
        self.assertEqual(user_login.status_code, 201)
        token = ast.literal_eval(user_login.data.decode())
        return token['token']


class TestAuth(unittest.TestCase):
    """"Testcase for blueprint for authentication
    "" Will create a user in the db and drop it after test execution
    """

    def setUp(self):
        self.app = app
        self.app.config.from_object(app_config['testing'])
        self.client = self.app.test_client
        self.user_details = json.dumps({'password': 'testing_p@ssword',
                             'username': 'new_user'
                            })

        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_register_user(self):
        """"Method to test a successful registration
        """
        user_register = self.client().post('/signup', data=self.user_details, content_type="application/json")
        
        result = json.loads(user_register.data)
        
        self.assertEqual(result['message'], "registered successfully")
        self.assertEqual(user_register.status_code, 201)

    def test_user_login(self):
        """"Method to test successful user login
        """
        user_register = self.client().post('/signup', data=self.user_details, content_type="application/json")
        self.assertEqual(user_register.status_code, 201)

        user_login = self.client().post('/login', data=self.user_details, content_type="application/json")

        self.assertEqual(user_login.status_code, 201)


    def test_user_logged_in_user_can_get_books(self):
        """"Method to test fetching books with logged in user
        """
        logintoken = getLoginToken(self)
        headers = {
            'content-type': "application/json",
            'x-access-token': logintoken
        }
        fetch_books = self.client().get('/bookapi/books', data=self.user_details, content_type="application/json", headers=headers)
        response = fetch_books.data.decode()
        self.assertEqual(fetch_books.status_code, 200)
        self.assertEqual(ast.literal_eval(response), {"Books":[]})


    def test_user_without_valid_token_cannot_get_books(self):
        """Method to check errors with invalid login
        """
        headers = {
            'content-type': "application/json",
            'x-access-token': 'invalid-token'
        }
        fetch_books = self.client().get('/bookapi/books', data=self.user_details, content_type="application/json", headers=headers)
        response = fetch_books.data.decode()
        self.assertEqual(fetch_books.status_code, 401)
        self.assertEqual(ast.literal_eval(response)['message'], 'Invalid token!')

    def test_user_logged_in_user_can_add_books(self):
        """[summary]
        """
        pass