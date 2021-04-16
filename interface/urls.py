from django.urls import path
from interface import views
from interface.views import (
    StudentView,
    TeacherView,
    StudentMoreInfo,
    TeacherMoreInfo,
    StaffMoreInfo,
    StaffView
)
from encryption.views import(
    home,
    encrypt,
    decrypt,
    encrypted,
    decrypted
)


urlpatterns = [
    path('', views.cover, name='cover'),
    path('contact', views.contact, name='contact'),
    path('categories', views.categories, name='categories'),
    path('students', StudentView.as_view(), name='students'),
    path('teachers', TeacherView.as_view(), name='teachers'),
    path('staff_records', StaffView.as_view(), name='staffs'),
    path('students/<int:pk>/', StudentMoreInfo.as_view(), name='more-info'),
    path('teachers/<int:pk>/', TeacherMoreInfo.as_view(), name='more-info-teachers'),
    path('staffs/<int:pk>/', StaffMoreInfo.as_view(), name='more-info-staffs'),
    path('help', views.help, name='help'),
    path('encryption/', home, name='encryption'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
    path('encrypted/', encrypted, name='encrypted'),
    path('decrypted/', decrypted, name='decrypted'), 
]