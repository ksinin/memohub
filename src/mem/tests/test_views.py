from django.test import TestCase, Client
from django.urls import reverse
from mem.models import Mem, UserFollowing
import json


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.addmem_url = reverse('addmem')
        self.yourmemes_url = reverse('yourmemes')

    def test_AddMemView_Get(self):
        response = self.client.get(self.addmem_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addmem.html')

    def test_YourMemView_Get(self):
        response = self.client.get(self.addmem_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'yourmemes.html')




