from django.urls import path, include
import requests

from . import views

urlpatterns = [
    path('', views.mainView, name = 'mainView'),
    path('search/', views.searchView, name = 'searchView'),
    path('classes/', views.homeView, name = 'homeView'),
    path('departments/', views.DeptSearchView, name = 'department_list'),
    path('departments/<str:subject>/', views.ClassFilterView.as_view(), name = 'class_list'),
    path('submission/', views.SubmissionView, name = 'SubmissionView'),
    path('resubmission/', views.ResubmissionView, name = "ResubmissionView"),
    path('departments/<str:subject>/<str:catalog_number>/', views.ClassInfo, name = 'class_info'),
    path('allbooks/', views.AllBookView.as_view(), name = 'allbooks'),
    path('details/<int:book_id>/', views.display_book_info, name = 'bookdetails'),
    path('update_profile/', views.UpdateProfileView, name = 'updateprofileview'),
    path('profile/', views.profileView, name = 'accountView'),
    path('removeFavorite', views.removeFavorite, name = 'removeFavorite'),
    path('addFavorite', views.addFavorite, name = 'addFavorite'),
    path('removeFriend', views.removeFriend, name = 'removeFriend'),
    path('addFriend', views.addFriend, name = 'addFriend'),
    path('removeListing', views.removeListing, name = 'removeListing'),
    path('requestFriend', views.requestFriend, name = 'requestFriend'),
    path('removeFriendRequest', views.removeFriendRequest, name = 'removeFriendRequest'),
]