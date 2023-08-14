from django.contrib.auth.models import User
from .models import Match
from rest_framework import status
from rest_framework.test import APITestCase

# Testing CRUD functionality, as well as some permissions
# for the Match App


class MatchCreateTests(APITestCase):
    # Check creation of a match object
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester11', password='pass1234')
        self.client.login(username='tester11', password='pass1234')

    def test_create_match(self):
        url = '/matches/'
        data = {
            'title': 'Testmatch',
            'match_date': '15 Aug 2023',
            'match_location': 'Geneva Range X',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 1)
        self.assertEqual(Match.objects.get().title, 'Testmatch')
        # print(response.data)

    def test_create_match_without_mandatory_fields(self):
        # Try to create object with missing match_date and match_location,
        # which are mandatory fields
        url = '/matches/'
        data = {'title': 'Testmatch'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MatchRetrieveTests(APITestCase):
    # Test retrieval of match test object, after creating one
    def setUp(self):
        # date has to be in the format of the DB
        self.user = User.objects.create_user(
            username='tester11', password='pass1234')
        self.match = Match.objects.create(
            owner=self.user, title='Testmatch',
            match_date='2023-08-15', match_location='Geneva Range X')

    def test_retrieve_match(self):
        # check for correct retrieval - match_date is now in the updated
        # time format, as we set it
        url = f'/matches/{self.match.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Testmatch')
        self.assertEqual(response.data['match_date'], '15 Aug 2023')


class MatchUpdateTests(APITestCase):
    # check update a match object, with a new title
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester11', password='pass1234')
        self.match = Match.objects.create(
            owner=self.user, title='Testmatch',
            match_date='2023-08-15',
            match_location='Geneva Range X')
        self.client.login(username='tester11', password='pass1234')

    def test_update_match(self):
        # update the match title
        url = f'/matches/{self.match.id}/'
        data = {'title': 'Updated Testmatch'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.match.refresh_from_db()
        self.assertEqual(self.match.title, 'Updated Testmatch')


class MatchUpdatePermissionTests(APITestCase):
    # check if one user cannot update the match element of the other
    # setup two user with each having a match object
    def setUp(self):
        self.user11 = User.objects.create_user(
            username='tester11', password='pass1234')
        self.user12 = User.objects.create_user(
            username='tester12', password='pass1234')
        self.match1 = Match.objects.create(
            owner=self.user11, title='Testmatch1',
            match_date='2023-08-15',
            match_location='Geneva Range X')
        self.match2 = Match.objects.create(
            owner=self.user12, title='Testmatch2',
            match_date='2023-08-16',
            match_location='Geneva Range Y')

    def test_update_other_users_match(self):
        # Log in as tester 11
        self.client.login(username='tester11', password='pass1234')

        # Try to update the match created by tester12
        url = f'/matches/{self.match2.id}/'
        data = {'title': 'Updated Testmatch'}
        response = self.client.patch(url, data, format='json')

        # We expect a 403 permission denied response
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Ensure that the match title of tester12 has not changed
        self.match2.refresh_from_db()
        self.assertEqual(self.match2.title, 'Testmatch2')


class MatchDeleteTests(APITestCase):
    # check if owner can delete the match object
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester11', password='pass1234')
        self.match = Match.objects.create(
            owner=self.user, title='Testmatch',
            match_date='2023-08-15',
            match_location='Geneva Range X')
        self.client.login(username='tester11', password='pass1234')

    def test_delete_match(self):
        # delete the created match object
        url = f'/matches/{self.match.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Match.objects.count(), 0)
