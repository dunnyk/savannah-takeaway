
from unittest.mock import patch, Mock
from .base_test import TestBaseCase
from rest_framework import status


class OrderTest(TestBaseCase):

    @patch('order.views.send_sms', Mock(return_value=True))
    def test_create_valid_order_succeeds(self):
        response = self.create_valid_order()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', res)
        self.assertEqual(res['message'], 'your order is placed successfully')

    def test_create_order_without_token_fails(self):
        response = self.create_order_without_token()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', res)
        self.assertEqual(
            res['detail'], 'Authentication credentials were not provided.')

    def test_create_order_with_invalid_details_fails(self):
        response = self.create_order_with_invalid_details()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', res)

    @patch('order.views.send_sms', Mock(return_value=True))
    def test_retrieve_single_order(self):
        response = self.retrieve_single_order()
        res = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(res['message'], 'Order pulled successfully')
