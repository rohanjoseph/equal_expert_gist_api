from django.test import TestCase,client

# Create your tests here.

class GistAPITestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = client.Client()

    def test_get_gists_valid_user(self):
        response = self.client.get('/getdata/octocat/')
        self.assertEqual(response.status_code, 200)

    def test_get_gists_invalid_user(self):
        response = self.client.get('/getdata/iamnotauser1234/')
        self.assertEqual(response.status_code, 404)
    
    def test_get_gists_no_user(self):
        response = self.client.get('/getdata//')
        self.assertEqual(response.status_code, 404)

    def test_get_gists_empty_username(self):
        response = self.client.get('/getdata//')
        self.assertEqual(response.status_code, 404)
