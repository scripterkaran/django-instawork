from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from users.models import User
from users.serializers import UserSerializer
from django.test.client import RequestFactory


class AccountTests(APITestCase):

    def test_create_member(self):
        url = reverse('user-list')
        data = {
            "username": "Cersei.Lannister",
            "first_name": "Cersei",
            "last_name": "Lannister",
            "phone_number": "+93322212212",
            "email": "queenofwesteros@got.com",
            "role": 2
        }
        response = self.client.post(url, data, format='json')
        context = {'request': RequestFactory().post(url)}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().first_name, 'Cersei')
        self.assertEqual(User.objects.get().role, User.STAFF)
        self.assertIsInstance(response.data, dict)  # check the response data to be dict
        serializer = UserSerializer(instance=User.objects.get(), context=context)
        self.assertEqual(serializer.data, response.data)

    def test_create_admin(self):
        url = reverse('user-list')
        data = {
            "username": "Ned.Stark",
            "first_name": "Ned",
            "last_name": "Stark",
            "phone_number": "+913344556677",
            "email": "dead@got.com",
            "role": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().role, User.ADMIN)

    def test_invalid_member_creation(self):
        url = reverse('user-list')
        data = {
            "username": "white.walker",
            "first_name": f"{'white' * 256}",  # max length for first_name is 32
            "last_name": "walker",
            "phone_number": "+913344556677",
            "email": "many@got.com",
            "role": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertIsInstance(response.data.get('first_name')[0], ErrorDetail)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_member_creation_role(self):
        url = reverse('user-list')
        data = {
            "username": "John.Snow",
            "first_name": "John",
            "last_name": "Snow",
            "phone_number": "+913344556677",
            "email": "kingofthenorth@got.com",
            "role": 4  # Wrong
        }
        response = self.client.post(url, data, format='json')
        self.assertIsInstance(response.data.get('role')[0], ErrorDetail)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_member(self):
        create_url = reverse('user-list')
        data = {
            "username": "Hodor.Hodor",
            "first_name": "Hodor",
            "last_name": "Hodor",
            "phone_number": "+93322212212",
            "email": "holdthedoor@got.com",
            "role": 2
        }
        create_response = self.client.post(create_url, data, format='json')
        update_url = reverse('user-detail', kwargs={'pk': create_response.data.get('id')})
        updated_fields = {
            "first_name": "Hodor (dead)",
            "role": 1
        }
        update_response = self.client.patch(update_url, updated_fields, format='json')  # patch request
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data.get('first_name'), updated_fields.get('first_name'))
        self.assertEqual(User.objects.get().first_name, update_response.data.get('first_name'))
        self.assertEqual(User.objects.get().role, update_response.data.get('role'))

    def test_delete_member(self):
        instance = User.create_dummy_data()
        url = reverse('user-detail', kwargs={'pk': instance.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')  # check for delete resource
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
