from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Laboratorio

class Iniciotests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/inicio/")
        self.assertEqual(response.status_code,200)