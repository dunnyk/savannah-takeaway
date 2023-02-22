from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from authentication.models import User
from order.models import Order


class TestBaseCase(APITestCase):

    def setUp(self):
        self.create_order_url = api_reverse('order:orders-create')
        # self.retrieve_order_url = api_reverse('order:retrieve-order')
        self.login_url = api_reverse('authentication:customer-login')

        # signup a user
        self.customer = User.objects.create(
            first_name='John1',
            last_name='Doe1',
            phone_number='+254706193094',
            username='john1',
            email='arrow1@gmail.com',
            password='Pass@123',
            is_active=True,
            is_staff=False
        )

        # setup user login credentials
        self.valid_user_login_details = {
            "email": "arrow1@gmail.com",
            "password": "Pass@123",
        }

        # get token from the login method
        self.token = self.login_user()

        self.valid_order_data = {
            'amount': 200,
            'item': 'Another Test Item'
        }

        self.invalid_order_data = {
            'item': 'Another Test Item'
        }

    def login_user(self):
        """login user and return token"""
        token = self.customer.token
        # response = self.client.post(self.login_url, self.valid_user_login_details, format='json')
        return token

    def create_valid_order(self):
        """Create a new order, remember to pass the token"""

        response = self.client.post(self.create_order_url, self.valid_order_data, format='json',
                                    HTTP_AUTHORIZATION='token {}'.format(self.token))

        return response

    def create_order_without_token(self):
        """Create a new order, remember to pass the token"""

        response = self.client.post(
            self.create_order_url, self.valid_order_data, format='json')

        return response

    def create_order_with_invalid_details(self):
        """Create a new order, remember to pass the token"""

        response = self.client.post(self.create_order_url, self.invalid_order_data, format='json',
                                    HTTP_AUTHORIZATION='token {}'.format(self.token))

        return response

    def retrieve_single_order(self):
        self.create_valid_order()

        order = Order.objects.filter(
            item=self.valid_order_data['item']).first()
        response = self.client.get(
            api_reverse('order:retrieve-order', args=[order.id]),
            HTTP_AUTHORIZATION='token {}'.format(self.token))
        return response
