from http import HTTPStatus

from django.test import TestCase, Client

from api import models


class TaskiApiTestCase(TestCase):
    def setUp(self):
        self.cl = Client()

    def test_list_exists(self):
        respose = self.cl.get('/api/tasks/')
        self.assertEqual(respose.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        data = {
            'title': 'порно',
            'description': 'описание'
        }
        response = self.cl.post('/api/tasls/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(models.Task.objects.filter(title='порно').exists())
