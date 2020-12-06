from django.test import TestCase, Client
from django.contrib.auth import get_user_model

# generate url for django project
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@lys.com',
            password='test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='normal_user@lys.com',
            password='test1234',
            name='Test user full name'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.admin_user.email)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code , 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code , 200) 

         