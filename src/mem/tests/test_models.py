from django.test import TestCase


@classmethod
def setUpTestData(cls):
    print("setUpTestData: Run once to set up non-modified data for all class methods.")
    pass


def setUp(self):
    print("setUp: Run once for every test method to setup clean data.")
    pass
