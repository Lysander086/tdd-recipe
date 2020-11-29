from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_wiht_email_successful(self):
        email = 'test@lys.com'
        password = "TestPass123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """"""
        email = 'test@LYS.com'
        user = get_user_model().objects.create_user(email , 'test123')

        self.assertEqual(user.email , email.lower())


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser('test@lys.comn', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)