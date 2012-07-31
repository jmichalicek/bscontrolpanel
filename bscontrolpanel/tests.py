from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

#TODO: Template tag test cases

TEST_USERNAME = 'test_user'
TEST_PASSWORD = 'testpass'

class LoginViewTests(TestCase):
    """Test the login view"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(TEST_USERNAME, password=TEST_PASSWORD)

    def test_basic_tests(self):
        response = self.client.get(reverse('bscontrolpanel:login'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual('bscontrolpanel/login.html', response.templates[0].name)

    def test_login_form_submit(self):
        form_data = {'username': TEST_USERNAME,
                     'password': TEST_PASSWORD,
                     'next': reverse('bscontrolpanel:index') #this is on the url and/or a hidden form element
                     }

        response = self.client.post(reverse('bscontrolpanel:login'), form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response._headers['location'][1],
                         'http://testserver%s' %reverse('bscontrolpanel:index'))

class IndexViewTests(TestCase):
    """Test the index view"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(TEST_USERNAME, password=TEST_PASSWORD)

    def test_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('bscontrolpanel:index'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response._headers['location'][1],
                         'http://testserver%s?next=%s' %(reverse('bscontrolpanel:login'),
                                                         reverse('bscontrolpanel:index')))

    def test_logged_in(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
        response = self.client.get(reverse('bscontrolpanel:index'))
        self.assertEqual(response.status_code, 200)
