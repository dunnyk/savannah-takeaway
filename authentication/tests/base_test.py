from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


class TestBaseCase(APITestCase):

    def setUp(self):
        self.signup_url = api_reverse('authentication:customers-signup')
        self.login_url = api_reverse('authentication:customer-login')

        self.valid_user = {
            "first_name": "gg",
            "last_name": "gm",
            "email": "g@gmail.com",
            "username": "gg",
            "password": "Pass@123",
            "phone_number": "+25406193094"
        }

        self.user_missing_email = {
            "first_name": "gg",
            "last_name": "gm",
            "username": "gg",
            "password": "Pass@123",
            "phone_number": "+25406193094"
        }

        self.user_invalid_pass = {
            "first_name": "gg",
            "last_name": "gm",
            "username": "gg",
            "email": "g@gmail.com",
            "password": "Pas",
            "phone_number": "+25406193094"
        }

        self.user_invalid_username = {
            "first_name": "gg",
            "last_name": "gm",
            "email": "g@gmail.com",
            "password": "Pass@123",
            "phone_number": "+25406193094"
        }

        self.user_missing_first_name = {
            "last_name": "gm",
            "email": "g@gmail.com",
            "username": "gg",
            "password": "Pass@123",
            "phone_number": "+25406193094"
        }

        self.user_missing_last_name = {
            "first_name": "gm",
            "email": "g@gmail.com",
            "username": "gg",
            "password": "Pass@123",
            "phone_number": "+25406193094"
        }

    def signup_user(self):
        response = self.client.post(
            self.signup_url, self.valid_user, format='json')
        return response

    def signup_user_without_email(self):
        response = self.client.post(
            self.signup_url, self.user_missing_email, format='json')
        return response

    def signup_user_with_invalid_password(self):
        response = self.client.post(
            self.signup_url, self.user_invalid_pass, format='json')
        return response

    def signup_user_without_username(self):
        response = self.client.post(
            self.signup_url, self.user_invalid_username, format='json')
        return response

    def signup_user_without_first_name(self):
        response = self.client.post(
            self.signup_url, self.user_missing_first_name, format='json')
        return response

    def signup_user_without_last_name(self):
        response = self.client.post(
            self.signup_url, self.user_missing_last_name, format='json')
        return response
