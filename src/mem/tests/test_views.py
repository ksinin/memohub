from django.test import TestCase, Client
from django.urls import reverse
from mem.models import Mem, UserFollowing
import json

from mem.tests.factories import UserFactory


class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_AddMemView_Get(self):
        response = self.client.get(reverse('addmem'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addmem.html')

    def test_YourMemView_Get(self):
        user = UserFactory()

        response = self.client.get(reverse('yourmemes', args=[user.username]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'yourmemes.html')




