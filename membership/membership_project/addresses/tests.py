from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User
from .models import Address
from rest_framework.authtoken.models import Token
# Create your tests here.

class AddressAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.address = Address.objects.create(user=self.user, street='792 stapleford', city='Prattville', state='AL',postal_code='36066')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)
    
    def target_get_addresses_unauthroized(self):
        self.client.logout()
        url = reverse('address-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_addresses(self):
        url = reverse('address-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
    
    def test_create_address(self):
        url = reverse('create-user-address', kwargs={'user_id':self.user.id})
        data = {
            'street': '792 stapleford',
            'city':'Prattville',
            'state': 'AL',
            'postal_code':'36066'
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_address(self):
        url = reverse('address-detail', kwargs={'pk': self.address.pk}) + "update"
        data = {
            'street':'811 thomas st',
        }
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertEqual(self.address.street, '792 stapleford')
    
    def test_delete_address(self):
        url = reverse('address-detail', kwargs={'pk':self.address.pk})+ "delete"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Address.objects.filter(pk=self.address.pk).exists())