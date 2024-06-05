from django.views.generic import ListView, DetailView
from account.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .forms import VakilSearchForm
# from account.mixins import AuthorAccessMixin
# from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category,Vakil,Riyasat,Comision
from django.db.models import Q
from django.views import View
# Create your views here.
class ArticleList(View):
	
	def get(self,request):
		article = Article.objects.published()
		paginate_by = 5
		return render(request,'home/index.html',{'article':article})


class ArticleDetail(View):
	def get(self,request,slug):
		
		article = get_object_or_404(Article.objects.published(), slug=slug)
		# ip_address = self.request.user.ip_address
		# if ip_address not in article.hits.all():
		# 	article.hits.add(ip_address)

		return render(request,'home/post_detail.html',{'article':article})

class VokalaView(View):
	form_class = VakilSearchForm
	def get(self,request):
		vakils = Vakil.objects.all()
		if request.GET.get('search') :
			vakils = vakils.filter(name__contains = request.GET['search'])
		return render(request,'home/vokala.html',{'vakils':vakils,'form':self.form_class})
class ArticlePreview(DetailView):
	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Article, pk=pk)


# class VakilHamedan(View):
# 	def get(self,request):
# 		hamedanvakil = Vakil.objects.filter(city="hamedan")
# 		return render(request,'home/hamedanvokala.html',{'hamedanvakils':hamedanvakil,})

class CategoryList(ListView):
	paginate_by = 5
	template_name = 'blog/category_list.html'

	def get_queryset(self):
		global category
		slug = self.kwargs.get('slug')
		category = get_object_or_404(Category.objects.active(), slug=slug)
		return category.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context


class AuthorList(ListView):
	paginate_by = 5
	template_name = 'blog/author_list.html'

	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context


class SearchList(ListView):
	paginate_by = 1
	template_name = 'blog/search_list.html'

	def get_queryset(self):
		search = self.request.GET.get('q')
		return Article.objects.published().filter(Q(description__icontains=search) | Q(title__icontains=search))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')
		return context

class VakilPage(View):
	def get(self,request,id):
		vakil = Vakil.objects.get(id=id)
		return render(request,'home/vakilpage.html',{'vakil':vakil})
class VakilCity(View):
	def get(self,request,city):
		vakils = Vakil.objects.filter(city=city)
		return render(request,'home/vakil_detail.html',{'vakils':vakils})

class Riyast(View):
	def get(self,request):
		heyatmodireh = Riyast.objects.all()
		return render(request,'home/index.html',{'heyatmodireh':heyatmodireh})


class ComisionView(View):
	def get(self,request,name):
		comision = Comision.objects.get(name=name)
		return render(request,'home/comision.html',{'comision':comision})