from django.test import TestCase
from repairs.models import Depo


class DepoModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.depo = Depo.objects.create(
            name='Фили',
            prefix='ФЛ',
        )

    def test_models_depo_have_correct_object_names(self):
        """Проверяем, что у модели Depo корректно отображается __str__."""
        depo = DepoModelTest.depo
        self.assertEqual(depo.name, str(depo))

    def test_models_depo_have_correct_prefix(self):
        """Проверяем, что у модели Depo корректно отображается prefix"""
        depo = DepoModelTest.depo
        self.assertEqual(depo.prefix, 'ФЛ')
