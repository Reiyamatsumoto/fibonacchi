# fibonacci/tests.py
from django.test import TestCase, Client
from django.urls import reverse

class FibonacciAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_input(self):
        response = self.client.get(reverse('fibonacci'), {'n': 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 55)

    def test_invalid_input(self):
        response = self.client.get(reverse('fibonacci'), {'n': -1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 400)
        self.assertEqual(response.json()['message'], 'Bad request.')
