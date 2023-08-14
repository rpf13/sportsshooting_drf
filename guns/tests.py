from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Gun
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


# Testing CRUD functionality, as well as some permissions
# for the Gun App

class GunCreateTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='shooter11', password='password1234')
        self.client.login(username='shooter11', password='password1234')

    def test_create_gun(self):
        url = '/guns/'
        data = {
            'brand': 'Glock',
            'gun_model': 'G17',
            'type': 'Handgun',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gun.objects.count(), 1)
        self.assertEqual(Gun.objects.get().brand, 'Glock')
        # print(response.data)

    def test_create_gun_with_large_image(self):
        # if if large images cannot be used, since we have the
        # limitation in place in the serializer
        url = '/guns/'
        image = Image.new('RGB', (5000, 5000))
        tmp_file = io.BytesIO()
        image.save(tmp_file, format='JPEG')
        tmp_file.seek(0)
        image_file = SimpleUploadedFile(
            'large_image.jpg', tmp_file.read(), content_type='image/jpeg')

        data = {
            'brand': 'Glock',
            'gun_model': 'G17',
            'type': 'Handgun',
            'image': image_file,
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Image with width larger than 4096px',
                      str(response.data))


class GunRetrieveTests(APITestCase):
    # check if logged in user can retreive a gun object
    def setUp(self):
        self.user = User.objects.create_user(
            username='shooter11', password='password1234')
        self.gun = Gun.objects.create(
            owner=self.user, brand='Glock', gun_model='G17', type='Handgun')

    def test_retrieve_gun(self):
        # login user first
        self.client.login(username='shooter11',
                          password='password1234')
        url = f'/guns/{self.gun.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], 'Glock')

    def test_unauthenticated_user_cannot_retrieve(self):
        # Attempt to retrieve gun object without logging in
        url = f'/guns/{self.gun.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GunUpdateTests(APITestCase):
    # check if logged in user can update a gun object
    def setUp(self):
        self.user = User.objects.create_user(
            username='shooter11', password='password1234')
        self.gun = Gun.objects.create(
            owner=self.user, brand='Glock', gun_model='G17', type='Handgun')
        # user needs to be logged in
        self.client.login(username='shooter11',
                          password='password1234')

    def test_update_gun(self):
        # update brand and model
        url = f'/guns/{self.gun.id}/'
        data = {'brand': 'SIG', 'gun_model': 'P320'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.gun.refresh_from_db()
        self.assertEqual(self.gun.brand, 'SIG')
        self.assertEqual(self.gun.gun_model, 'P320')


class GunDeleteTests(APITestCase):
    # check if logged in user can delete a gun oject
    def setUp(self):
        self.user = User.objects.create_user(
            username='shooter11', password='password1234')
        self.gun = Gun.objects.create(
            owner=self.user, brand='SIG', gun_model='P365', type='Handgun')
        # login user
        self.client.login(username='shooter11',
                          password='password1234')  # User logged in

    def test_delete_gun(self):
        url = f'/guns/{self.gun.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Gun.objects.count(), 0)
