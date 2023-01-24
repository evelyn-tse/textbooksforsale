from django.test import TestCase

from textbook_exchange.models import Book, Department, BookForm, Class

import datetime

class TestBookModel(TestCase):

    def setUp(self):
        self.testBook = Book.objects.create(title = 'The Host', author = 'James Bond', ISBN = 1234, price = 4)
        self.assertEqual(self.testBook.title, "The Host")

    def test_department(self):
        testDepartment = Department.objects.create(subject = "CS")
        self.assertEqual(testDepartment.subject, "CS")

    # def test_bookForm(self):
    #     testBookForm = BookForm(data={
    #         "model" : self.testBook,
    #         "fields" : ['The Host', 1234, 'James Bond', 4]
    #     })
    #     self.assertTrue(testBookForm.is_valid())

    def test_class(self):
        testClass = Class.objects.create(instructor = "Sheriff",
        instructor_email = "sheriff@virginia.edu",
        course_number = 3240,
        semester_code = 22,
        course_section = 17,
        subject = "CS",
        catalog_number = 123,
        description = "software development",
        units = "3",
        component = "LEC",
        class_capacity = 200,
        wait_list = 50,
        wait_cap = 78,
        enrollment_total = 132,
        enrollment_available = 68,
        topic = "building software",
        meeting_days = "TuesThurs",
        start_time = datetime.time(10, 33, 45),
        end_time = datetime.time(10, 33, 45),
        location = "Rice Hall")
        testClass.book.add(self.testBook)

        self.assertEqual(testClass.course_number, 3240)

        