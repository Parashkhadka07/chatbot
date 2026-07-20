from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class ChatBotAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('chat_bot')

    def test_chat_endpoint_returns_400_for_empty_message(self):
        response = self.client.post(self.url, data={'message': ''}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'No message provided')

    def test_chat_endpoint_returns_400_for_invalid_json(self):
        response = self.client.post(self.url, data='not-json', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Invalid JSON')
