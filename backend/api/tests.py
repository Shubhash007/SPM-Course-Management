from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class StaffTestCase(APITestCase):
    def test_staff_info(self):
        response = self.client.get('http://127.0.0.1:5000/staff')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
