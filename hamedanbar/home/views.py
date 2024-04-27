from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course

class HomeView(View):
	def get(self, request) :
		courses = Course.objects.all()
		return render(request, 'home/home.html',{'courses':courses})