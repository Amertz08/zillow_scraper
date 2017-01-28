from __future__ import absolute_import, unicode_literals, print_function

from flask_testing import TestCase

from app import db, create_app


class BaseTest(TestCase):
    BASE_URL = 'http://localhost:5000/'

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_setup(self):
        response = self.client.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
