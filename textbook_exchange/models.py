from django.db import models
from django.forms import ModelForm
from django.forms import modelformset_factory
from django.contrib.auth.models import User

# Create your models here.
# department model which follows the API call: http://luthers-list.herokuapp.com/api/deptlist?format=json
class Department(models.Model):
    subject = models.CharField(max_length = 10)

    def __str__(self):
        return self.subject
    

# class model which follows the API call: http://luthers-list.herokuapp.com/api/dept/CS/?format=json



class Book(models.Model):
    title = models.CharField(max_length = 100)
    ISBN = models.IntegerField()
    author = models.CharField(max_length = 50)
    price = models.IntegerField()
    condition = models.CharField(max_length = 10, default = "Good")
    course = models.CharField(max_length = 20, default="CS 3240")
    instructor = models.CharField(max_length = 50, default="none")
    seller = models.CharField(max_length = 20, default="evelyn8")


    def __str__(self):
        return self.title

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'ISBN', 'author', 'price', 'course']

class Course(models.Model):
    subject = models.CharField(max_length=10) 
    catalog_number = models.CharField(max_length=14)
    instructor = models.CharField(max_length=50, default="Unknown")

class Instructor(models.Model):
    instructor = models.CharField(max_length=80)
    def __str__(self):
        return self.instructor

class Class(models.Model):
    instructor = models.CharField(max_length=80)
    instructor_email = models.CharField(max_length=80)
    course_number = models.IntegerField()
    semester_code = models.IntegerField()
    course_section = models.IntegerField() 
    subject = models.CharField(max_length=10) # this is the department code
    catalog_number = models.IntegerField()
    description = models.CharField(max_length=100) # this is the course title
    units = models.CharField(max_length=10)
    component = models.CharField(max_length=10) # LEC vs LAB
    class_capacity = models.IntegerField()
    wait_list = models.IntegerField()
    wait_cap = models.IntegerField()
    enrollment_total = models.IntegerField()
    enrollment_available = models.IntegerField()
    topic = models.CharField(max_length=100)
    meeting_days = models.CharField(max_length=14)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    year = models.IntegerField(null=True)
    # major = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=15, null=True)

    def __str__(self) -> str:
        return super().__str__()




class FriendsList(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name="friends", blank=True)

    def __str__(self) -> str:
        return super().__str__()


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE, default=None)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, default=None)


    def __str__(self) -> str:
        return super().__str__()


class FavoriteBooks(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name="books", blank=True)

    def __str__(self) -> str:
        return super().__str__()

# class Profile(models.Model):
#     username = models.CharField(max_length=50, default = "")
#     first_name = models.CharField(max_length=50, default = "")
#     last_name = models.CharField(max_length=50, default = "")
#     email = models.EmailField(max_length=50, default = "")
#     major = models.CharField(max_length=100, default = "")
#     graduation_year = models.IntegerField(default=0000)
#     friends = models.ManyToManyField("Profile", blank=True)

#     def __str__(self):
#         return self.username