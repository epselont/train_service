from django.test import TestCase

from .models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            email='TesT@Tst.tSt',
            username='test',
            first_name='тест',
            patronymic='тестович',
            last_name='тестов',
            position='инженер',
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        user = UserModelTest.user
        field_str_text = {
            user: str(user),
        }
        for field, expected_object_name in field_str_text.items():
            with self.subTest(field=field):
                self.assertEqual(expected_object_name, str(field))

    def test_models_correct_role(self):
        """Проверка роли по умолчанию"""
        user = UserModelTest.user
        self.assertEqual(user.role, 'USER')

    def test_capitalize_names_and_positon(self):
        """Проверяем, что при сохранении в БД ФИО с заглавной буквы"""
        field_expected = {
            self.user.first_name: 'Тест',
            self.user.patronymic: 'Тестович',
            self.user.last_name: 'Тестов',
            self.user.position: 'Инженер',
        }
        for value, expected in field_expected.items():
            with self.subTest(value=value):
                self.assertEqual(value, expected)
