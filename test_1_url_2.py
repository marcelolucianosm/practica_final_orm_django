from django.test import SimpleTestCase, TestCase
from django.urls import reverse
import pytest

#from .models import Laboratorio

class Iniciotests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorio/add")
        self.assertEqual(response.status_code,200)

