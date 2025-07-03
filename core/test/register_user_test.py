from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from core.models import Company, CustomUser
from core.models.role import Role


class RegisterUserTest(APITestCase):

    def setUp(self):
        self.url = reverse('register')
        self.data = {
            'company_name': 'Test',
            'email': 'test@test.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'test123',
        }

    def test_register_user(self):
        """
        Test register user
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(name='Test')
        self.assertEqual(company.name,'Test')

        users = CustomUser.objects.filter(email='test@test.com').values('email', 'first_name', 'last_name')
        self.assertEqual(users[0], {
            'email': 'test@test.com',
            'first_name':'John',
            'last_name':'Doe',
        })

        created_user = CustomUser.objects.get(email='test@test.com')
        roles = created_user.roles.all()
        self.assertEqual(len(roles), 1)
        self.assertEqual(roles[0].role, Role.COMPANY_ADMIN)
        self.assertEqual(roles[0].company.name, 'Test')

        groups = created_user.groups.all()
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0].name, Role.COMPANY_ADMIN)

    def test_failed_duplicate_company_name(self):
        """
        Test duplicate company name
        """
        existing_company = Company.objects.create(name='Test')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['company_name'], ['Company name already registered'])

    def test_failed_duplicate_email(self):
        """
        Test duplicate email
        """
        existing_user = CustomUser.objects.create_user('test@test.com', 'test@test.com', 'test123')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'], ['Email already registered'])
