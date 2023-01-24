# #views.py
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from django.contrib.auth import get_user_model
# from django.test import TestCase, Client

# @login_required(login_url='/users/login')
# def secure(request):
#     user = request.user
#     return render(request, 'secure.html', {'email': user.email})



# #tests.py
# class SimpleTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         User = get_user_model()
#         user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
#         user.save()

#     def test_secure_page(self):
#         User = get_user_model()
#         self.client.login(username='temporary', password='temporary')
#         response = self.client.get('/accounts/login/', follow=True)
#         user = User.objects.get(username='temporary')
#         print(response.context)
#         self.assertEqual(response.context['user']., 'temporary@gmail.com')