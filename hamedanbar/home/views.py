from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

class HomeView(View):
	def get(self, request) :

		return render(request, 'home/index.html')
	

class VakilDetailView(View):
	def get(self, request) :

		return render(request, 'home/vakil_detail.html')
	
class PostDetailView(View):
	def get(self, request) :

		return render(request, 'home/post_detail.html')
	

class VokalaView(View):
	def get(self, request) :

		return render(request, 'home/vokala.html')