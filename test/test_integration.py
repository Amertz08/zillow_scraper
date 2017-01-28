from __future__ import absolute_import, print_function, unicode_literals

import os

from test import BaseTest


class TestIntegration(BaseTest):

    def test_config_set(self):
        self.assertIsNotNone(os.getenv('FLASK_CONFIG'), 'FLASK_CONFIG not set')

    def test_secret_key_set(self):
        self.assertIsNotNone(os.getenv('SECRET_KEY'), 'SECRET_KEY not set')

    def test_mysql_pass_set(self):
        self.assertIsNotNone(os.getenv('MYSQL_PASS'), 'MYSQL_PASS not set')
