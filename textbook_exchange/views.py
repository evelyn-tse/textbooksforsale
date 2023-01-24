from multiprocessing import context
from .models import Book, Department, Class, Course, FavoriteBooks, FriendRequest, FriendsList, Instructor
from django.views.generic import ListView, DetailView
from django.forms import modelformset_factory
from .forms import UserUpdateForm, ProfileUpdateForm
# from chat import views
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .filters import BookFilter, DepartmentFilter
from django.http import Http404
from django.contrib.auth.models import User
import requests


def mainView(request):
    return render(request, 'textbook_exchange/home.html')

def homeView(request):
    url = 'http://luthers-list.herokuapp.com/api/deptlist/'
    response = requests.get(url)
    data = response.json()
    context = {
        'data' : data,
    }
    return render(request, 'textbook_exchange/classes.html', context)

def searchView(request):

    books = Book.objects.all()

    filter = BookFilter(request.GET, queryset=books )
    books = filter.qs

    context = {'books':books,'filter':filter}
    return render(request, 'textbook_exchange/search.html', context)

def DeptSearchView(request):
    model = Department
    # template_name = 'textbook_exchange/departments.html'
    # context_object_name = 'department_list'

    Department.objects.all().delete()
    response = requests.get('http://luthers-list.herokuapp.com/api/deptlist/').json()
    for dept in response:
        Department.objects.create(subject=dept['subject'])
    
    departments = Department.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        data = departments.filter(subject__icontains = q)
    else:
        data = departments
    return render(request, "textbook_exchange/departments.html", {
        "departments": data
    })
    # departments = Department.objects.filter(subject=request.GET['searchbar'])
    # context = {'departments':departments}
    # return render(request, 'textbook_exchange/departments.html', context)

def ClassSearchView(request):
    classes = Class.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        data = classes.filter(catalog_number__icontains = q)
    else:
        data = classes
    return render(request, "textbook_exchange/classes.html", {"classes":data})
 
class ClassView(ListView):
    model = Class
    template_name = 'textbook_exchange/classes.html'
    context_object_name = 'class_load'

    def get_queryset(self):
        department = self.kwargs['subject']
        Class.objects.all().delete()

        response = requests.get('http://luthers-list.herokuapp.com/api/dept/' + department).json()
        for course in response:
            Class.objects.create(
                instructor=course['instructor']['name'],
                instructor_email=course['instructor']['email'],
                course_number=course['course_number'],
                semester_code=course['semester_code'],
                course_section=course['course_section'],
                subject=course['subject'],
                catalog_number=course['catalog_number'],
                description=course['description'],
                units=course['units'],
                component=course['component'],
                class_capacity=course['class_capacity'],
                wait_list=course['wait_list'],
                wait_cap=course['wait_cap'],
                enrollment_total=course['enrollment_total'],
                enrollment_available=course['enrollment_available'],
                topic=course['topic'],
                meeting_days=course['meetings'][0]['days'],
                # TODO: format time
                start_time=None,
                end_time=None,
                location=course['meetings'][0]['facility_description'],)

        return Class.objects.all()


def ResubmissionView(request):
    
    return render(request, 'textbook_exchange/resubmission.html')

def CourseView(request):
    model = Course
    department_list = Department.objects.all()
    Course.objects.all().delete()
    for department in department_list:
        depart = department.subject
        response = requests.get('http://luthers-list.herokuapp.com/api/dept/' + depart).json()
        for x in response:
            if(x['instructor']['name'] == "-"):
                instruct = "N/A"
            else:
                instruct = x['instructor']['name']
            if (Course.objects.filter(subject=x['subject'], catalog_number=x['catalog_number'], instructor = instruct).exists()):
                depart = depart
            else:
                Course.objects.create(
                subject=x['subject'],
                catalog_number=x['catalog_number'],
                instructor=instruct)
    return redirect('ResubmissionView')

def InstructorView(request):
    model = Instructor
    department_list = Department.objects.all()
    for department in department_list:
        depart = department.subject
        response = requests.get('http://luthers-list.herokuapp.com/api/dept/' + depart).json()
        for x in response:
            if (Instructor.objects.filter(instructor=x['instructor']['name']).exists()):
                depart = depart
            else:
                Instructor.objects.create(
                instructor=x['instructor']['name'])
    return redirect('ResubmissionView')

def SubmissionView(request):
    try:
        courseInst = request.POST['course']
        num = courseInst.index("-")
        cour = courseInst[:num-1]
        instr = courseInst[num+2:]
        book = Book(title=request.POST['title'], ISBN = request.POST['isbn'], author = request.POST['author'], price = request.POST['price'], condition = request.POST['condition'], course = cour,instructor = instr, seller = request.POST['seller'])
        book.save()
        return redirect('ResubmissionView')
    except(KeyError):
        instructor_list = Instructor.objects.all().order_by("instructor")
        course_list = Course.objects.all().order_by("subject")
        context = {'instructors': instructor_list, 'courses': course_list}
        return render(request, 'textbook_exchange/textbooksubmission.html', context)


class AllBookView(ListView):
    model = Book
    template_name = 'textbook_exchange/bookdisplay.html'
    context_object_name = 'textbook_list'

    def display_all_textbooks(request):

        textbook_list = Book.objects.all()
        context = {'textbook_list': textbook_list}
        return render(request, 'textbook_exchange/bookdisplay.html',context)


def UpdateProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('accountView')

    else:
        u_form = UserUpdateForm(instance=request.user)
        

    context = {
        'u_form': u_form,
        
        

    }

    return render(request, 'textbook_exchange/update_profile.html', context)





class ClassInfoView(ListView):
    model = Class
    template_name = 'textbook_exchange/classinfo.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        department = self.kwargs['subject']
        Class.objects.all().delete()

        response = requests.get('http://luthers-list.herokuapp.com/api/dept/' + department).json()
        for course in response:
            Class.objects.create(
                instructor=course['instructor']['name'],
                instructor_email=course['instructor']['email'],
                course_number=course['course_number'],
                semester_code=course['semester_code'],
                course_section=course['course_section'],
                subject=course['subject'],
                catalog_number=course['catalog_number'],
                description=course['description'],
                units=course['units'],
                component=course['component'],
                class_capacity=course['class_capacity'],
                wait_list=course['wait_list'],
                wait_cap=course['wait_cap'],
                enrollment_total=course['enrollment_total'],
                enrollment_available=course['enrollment_available'],
                topic=course['topic'],
                meeting_days=course['meetings'][0]['days'],
                start_time=None,
                end_time=None,
                location=course['meetings'][0]['facility_description'],)

        return Class.objects.all()

def ClassInfo(request, subject, catalog_number):

    template_name = 'textbook_exchange/classinfo.html'
    book_list = Book.objects.all()
    full_name = subject + " " + str(catalog_number)
    books = []
    for book in book_list:
        if book.course == full_name:
            books.append(book)
    context = {
        'subject': subject,
        'catalog_number': catalog_number,
        'books': books,
    }
    return render(request, template_name, context)

class ClassFilterView(ListView):
    model = Class
    template_name = 'textbook_exchange/classes.html'
    context_object_name = 'class_list'


    def get_queryset(self):
        department = self.kwargs['subject']
        Class.objects.all().delete()

        response = requests.get('http://luthers-list.herokuapp.com/api/dept/' + department).json()
        catalog = []
        for course in response:
            if course['catalog_number'] not in catalog:
                catalog.append(course['catalog_number'])
                Class.objects.create(
                    instructor=course['instructor']['name'],
                    instructor_email=course['instructor']['email'],
                    course_number=course['course_number'],
                    semester_code=course['semester_code'],
                    course_section=course['course_section'],
                    subject=course['subject'],
                    catalog_number=course['catalog_number'],
                    description=course['description'],
                    units=course['units'],
                    component=course['component'],
                    class_capacity=course['class_capacity'],
                    wait_list=course['wait_list'],
                    wait_cap=course['wait_cap'],
                    enrollment_total=course['enrollment_total'],
                    enrollment_available=course['enrollment_available'],
                    topic=course['topic'],
                    meeting_days=course['meetings'][0]['days'],
                    # TODO: format time
                    start_time=None,
                    end_time=None,
                    location=course['meetings'][0]['facility_description'],)

        return Class.objects.all()


def display_book_info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'Book': book}
    return render(request, 'textbook_exchange/bookdetails.html', context)

def profileView(request):
    try:
        friends = FriendsList.objects.get(user=request.user)
        friends = friends.friends
    except:
        friends = []
    try:
        favorite_books = FavoriteBooks.objects.get(user=request.user)
        favorite_books = favorite_books.books
    except:
        favorite_books = []

    incoming_friend_requests = FriendRequest.objects.filter(receiver=request.user).all()
    outgoing_friend_requests = FriendRequest.objects.filter(sender=request.user).all()

    friend_requests = []
    books = Book.objects.all()
    books = books.filter(seller=request.user)
    context = {'books': books, 'friends': friends, 'favorites': favorite_books, 'incoming_friend_requests': incoming_friend_requests, 'outgoing_friend_requests': outgoing_friend_requests}
    return render(request, 'textbook_exchange/profile.html', context)

def addFavorite(request):
    try:
        favorite_books = FavoriteBooks.objects.get(user=request.user)
    except:
        FavoriteBooks.objects.create(user=request.user)
        favorite_books = FavoriteBooks.objects.get(user=request.user)
        favorite_books.save()
    
    book = request.POST['book']
    book = Book.objects.get(pk=book)
    favorite_books.books.add(book)
    favorite_books.save()
    return redirect('accountView')

def removeFavorite(request):
    favorite_books = FavoriteBooks.objects.get(user=request.user)
    book = request.POST['book']
    book = Book.objects.get(pk=book)
    favorite_books.books.remove(book)
    favorite_books.save()
    return redirect('accountView')

def removeListing(request):
    book = request.POST['book']
    book = Book.objects.get(pk=book)
    book.delete()
    return redirect('accountView')

def addFriend(request):
    # friends = FriendsList.objects.filter(user=request.user).first()
    try:
        friends = FriendsList.objects.get(user=request.user)
    except:
        FriendsList.objects.create(user=request.user)
        friends = FriendsList.objects.get(user=request.user)
        friends.save()
    friend = request.POST['friend']
    try:
        # friend = User.objects.filter(username=friend).first()
        friend = User.objects.get(username=friend)
    except:
        User.objects.create(username=friend)
        friend = User.objects.get(username=friend)
        friend.save()
    friends.friends.add(friend)
    friends.save()
    return redirect('accountView')

def removeFriend(request):
    friends = FriendsList.objects.get(user=request.user)
    friend = request.POST['friend']
    friend = User.objects.get(username=friend)
    friends.friends.remove(friend)
    friends.save()
    return redirect('accountView')

def requestFriend(request):
    friend = request.POST['friend']
    friend = User.objects.get(username=friend)

    if FriendRequest.objects.filter(sender=request.user, receiver=friend).exists():
        return redirect('accountView')

    if FriendRequest.objects.filter(sender=friend, receiver=request.user).exists():
        addFriend(request)
        FriendRequest.objects.filter(sender=friend, receiver=request.user).delete()

    else:
        FriendRequest.objects.create(sender=request.user, receiver=friend)

    return redirect('accountView')


def removeFriendRequest(request):
    print(request.POST['friend'])
    friend = request.POST['friend']
    friend = User.objects.get(username=friend)
    FriendRequest.objects.filter(sender=friend, receiver=request.user).delete()
    FriendRequest.objects.filter(sender=request.user, receiver=friend).delete()
    return redirect('accountView')

def chatView(request):
    return redirect('chat:checkview')