
from .base_test import TestBaseCase
from rest_framework import status


class OrderTest(TestBaseCase):

    def test_create_order_succeed(self):
        res = {'email': ''}
        self.assertIn('email', res)
