from django.test import SimpleTestCase
from django.urls import reverse, resolve

from textbook_exchange.views import ClassFilterView, homeView, ClassView, ResubmissionView, SubmissionView, DeptSearchView

class TestUrls(SimpleTestCase):

    def test_homeView_url_is_resolved(self):
        url = reverse("homeView")

        self.assertEquals(resolve(url).func, homeView)

    def test_department_list_url_is_resolved(self):
        url = reverse("department_list")

        self.assertEquals(resolve(url).func, DeptSearchView)
    
    def test_class_list_url_is_resolved(self):
        url = reverse("class_list", args=["className"])

        self.assertEquals(resolve(url).func.view_class, ClassFilterView)
    
    def test_SubmissionView_url_is_resolved(self):
        url = reverse("SubmissionView")

        self.assertEquals(resolve(url).func, SubmissionView)

    def test_ResubmissionView_url_is_resolved(self):
        url = reverse("ResubmissionView")

        self.assertEquals(resolve(url).func, ResubmissionView)
