from django.test import TestCase, Client
from django.urls import reverse
from textbook_exchange.models import Department, Book, BookForm, Class
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homeView_url = reverse("homeView")
        self.department_list_url = reverse("department_list")
        self.class_list_url = reverse("class_list", args=["className"])
        self.SubmissionView_url = reverse("SubmissionView")
        self.ResubmissionView_url = reverse("ResubmissionView")

    def test_homeView_GET(self):
        response = self.client.get(self.homeView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "textbook_exchange/classes.html")

    def test_department_list_GET(self):
        response = self.client.get(self.department_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "textbook_exchange/departments.html")

    def test_class_list_GET(self):
        response = self.client.get(self.class_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "textbook_exchange/classes.html")

    def test_SubmissionView_GET(self):
        response = self.client.get(self.SubmissionView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "textbook_exchange/textbooksubmission.html")

    def test_ResubmissionView_GET(self):
        response = self.client.get(self.ResubmissionView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "textbook_exchange/resubmission.html")

