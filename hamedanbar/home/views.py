from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

class HomeView(View):
	def get(self, request) :

		return render(request, 'home/home.html')