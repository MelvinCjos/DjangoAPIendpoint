from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile

class ProfileAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_profile_create(self):
        url = reverse('profile_create')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().name, 'John Doe')

    def test_profile_update(self):
        profile = Profile.objects.create(name='Jane Smith', email='jane@example.com')
        url = reverse('profile_update', args=[profile.id])
        data = {'name': 'Jane Brown'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get().name, 'Jane Brown')
