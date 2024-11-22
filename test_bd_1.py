from django.test import TestCase
from laboratorio.models import Laboratorio

class MiModeloTestCase(TestCase):

    def setUp(self):
        
        Laboratorio.objects.create(laboratorio='Laboratorio 1', ciudad='Ciudad 1', pais='Pais 1')

    def test_modelo_guardado_correctamente(self):
        """
        Prueba que el modelo guarda correctamente los datos.
        """
        # Recupera el objeto de la base de datos simulada
        objeto = Laboratorio.objects.get(laboratorio='Laboratorio 1')
        
        # Asegúrate de que los datos son correctos
        self.assertEqual(objeto.ciudad, 'Ciudad 1')

    def test_modelo_filtro(self):
        """
        Prueba que los filtros funcionan correctamente.
        """
        # Usa el filtro para encontrar el objeto
        objeto = Laboratorio.objects.filter(laboratorio='Laboratorio 1').first()
        
        self.assertIsNotNone(objeto)
        self.assertEqual(objeto.ciudad, 'Ciudad 1')
