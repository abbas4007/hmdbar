from django.views.generic import ListView, DetailView
from django.contrib import admin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VakilSearchForm,AdminContactForm
from .models import Article, Category, Vakil, Riyasat, Comision, ComisionVarzeshi, ArticleImage
from django.db.models import Q
from django.views import View
# Create your views here.

class ArticleList(View):
	def get(self,request):
		article = Article.objects.published()
		heyatmodireh = Riyasat.objects.all()
		paginator = Paginator(article, 3)  # Show 25 contacts per page.
		page_number = request.GET.get("page")
		page_obj = paginator.get_page(page_number)
		return render(request,'home/index.html',{'article':article,'heyatmodireh':heyatmodireh,"page_obj": page_obj})


class ArticleDetail(View):
	def get(self,request,slug):
		article = get_object_or_404(Article.objects.published(), slug=slug)
		images = ArticleImage.objects.filter(article = article)
		return render(request, 'home/post_detail.html', {'article' : article, 'images' : images})


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
	# paginate_by = 2
	def get(self,request,city):
		vakils = Vakil.objects.filter(city=city)
		paginator = Paginator(vakils, 5)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'home/vakil_detail.html',{'vakils':vakils,'page_obj': page_obj})



class ComisionView(View):
	def get(self,request):
		comi = Comision.objects.all()
		return render(request,'home/comision.html',{'comi':comi})


class ComisionDetailView(View):
	def get(self,request):
		com = ComisionVarzeshi.objects.all()
		return render(request,'home/comisiondetail.html',{'com':com})

class UpdateImageView(View):
	def post(self,request):
		selected_action = request.POST.getlist('_selected_action')
		if selected_action :
			model_admin = admin.site._registry[Vakil]
			print(Vakil.objects.filter(pk__in = selected_action))
			print('mm')
			return model_admin.update_image(request, Vakil.objects.filter(pk__in = selected_action))

		return redirect('/')


class Contact(View):

	form_class = AdminContactForm
	def get(self,request):
		return render(request,'home/contact.html',{'form':self.form_class})


