import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User, Notes


class TestUserViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'name': 'Андрей',
                               'birthday_year': 1999}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'name': 'Андрей',
                               'birthday_year': 1999}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = User.objects.create(name='Андрей', birthday_year=1999)
        client = APIClient()
        response = client.get(f'/api/users/{User.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_edit_guest(self):
        author = User.objects.create(name='Андрей', birthday_year=1999)
        client = APIClient()
        response = client.put(f'/api/users/{User.id}/', {'name':'Маша',
                               'birthday_year': 1980})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_edit_admin(self):
        author = User.objects.create(name='Андрей', birthday_year=1999)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{User.id}/', {'name':'Маша',
                               'birthday_year': 1980})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = User.objects.get(id=author.id)
        self.assertEqual(author.name, 'Маша')
        self.assertEqual(author.birthday_year, 1980)
        client.logout()
    

class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestNotesViewSet(APITestCase):
    
    def test_get_list(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = User.objects.create(name='Андрей', birthday_year=1999)
        notes = Notes.objects.create(name='Пиковая дама', author=author)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/notes/{Notes.id}/', {'name': 'Руслан и Людмила', 'author': Notes.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        notes = Notes.objects.get(id=notes.id)
        self.assertEqual(notes.name,'Руслан и Людмила')
    