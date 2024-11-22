from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioTestCase(TestCase):

    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(laboratorio="Laboratorio 99", ciudad='Limache')

    def test_laboratorio_detalle_url(self):
        url = reverse('upd_laboratorio', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.laboratorio.laboratorio)
