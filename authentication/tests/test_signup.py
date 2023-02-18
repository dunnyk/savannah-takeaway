
from .base_test import TestBaseCase
from rest_framework import status


class RegistrationTest(TestBaseCase):

    def test_signup_user_succeed(self):
        response = self.signup_user()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('email', res)

    def test_signup_user_without_email_fails(self):
        response = self.signup_user_without_email()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', res)

    def test_signup_user_invalid_password_fails(self):
        response = self.signup_user_with_invalid_password()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', res)

    def test_signup_user_without_username_fails(self):
        response = self.signup_user_without_username()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', res)

    def test_signup_user_without_first_name(self):
        response = self.signup_user_without_first_name()
        result = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', result)

    def test_signup_user_without_last_name(self):
        response = self.signup_user_without_last_name()
        result = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', result)
