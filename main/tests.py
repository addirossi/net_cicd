from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestProducts(TestCase):
    def setUp(self) -> None:
        self.payload = {'name': 'Apple IPhone 13',
                        'description': 'Нормас телефон',
                        'price': 109.99}

    def test_create_product_without_price(self):
        data = self.payload.copy()
        data.pop('price')
        client = APIClient()
        url = reverse('create-product')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_create_product_without_name(self):
        data = self.payload.copy()
        data.pop('name')
        client = APIClient()
        url = reverse('create-product')
        response = client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.data)