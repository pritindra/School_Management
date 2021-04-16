from django.shortcuts import render, get_object_or_404
from interface.models import Students, Teachers, Staffs
import sys
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def cover(request):
    return render(request, "interface/cover.html")

# @login_required
def contact(request):
    return render(request, "interface/contact.html")

# @login_required
def categories(request):
    return render(request, "interface/categories.html")

class StudentView(ListView):
    model = Students
    template_name = 'interface/students.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class TeacherView(ListView):
    model = Teachers
    template_name = 'interface/teachers.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class StaffView(ListView):
    model = Staffs
    template_name = 'interface/staffs.html'
    context_object_name = 'staffs'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class StudentMoreInfo(DetailView,LoginRequiredMixin):
    model = Students
    template_name = 'interface/more_info.html'
    context_object_name = 'student'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class TeacherMoreInfo(DetailView,LoginRequiredMixin):
    model = Teachers
    template_name = 'interface/more_info_teachers.html'
    context_object_name = 'teacher'

class StaffMoreInfo(DetailView,LoginRequiredMixin):
    model = Staffs
    template_name = 'interface/more_info_staffs.html'
    context_object_name = 'staff'

# @login_required
def help(request):
    return render(request, "interface/help.html")
