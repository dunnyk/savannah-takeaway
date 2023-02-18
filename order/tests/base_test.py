from matplotlib.pyplot import cla
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


class TestBaseCase(APITestCase):

    def setup(self):
        self.orders_url


        # signup a user


        # setup user login credentials

        # get token from the login method
        self.token = login_user()


    def login_user(self):
        """login user and return token"""
        pass


    def create_valid_order(self):
        """Create a new order, remember to pass the token"""
        pass

    def create_order_with_invalid_details(self):
        """Create order with invalid amount"""

    def create_order_if_not_loggedin(self):
        pass