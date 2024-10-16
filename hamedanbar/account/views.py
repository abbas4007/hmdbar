from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from home.models import Article,Vakil,Riyasat

from .forms import ImageForm


# Create your views here.
class ArticleList(ListView):
    model = Article
    paginate_by = 6
    template_name = "account/home.html"

    # def get_queryset(self):
    #     return Article.objects.all()


class ArticleCreate(CreateView):
    model = Article
    fields =  '__all__'
    template_name = "account/article-create-update.html"
    success_url = reverse_lazy('account:home')



class ArticleUpdate(UpdateView):
    model = Article
    template_name = "account/article-create-update.html"
    fields =  '__all__'

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = "account/article_confirm_delete.html"

class AddVakil(CreateView):
    model = Vakil
    fields =  '__all__'
    template_name = "account/vakil-create-update.html"
    success_url = reverse_lazy('account:home')


class vakileList(ListView):
    template_name = "account/vakil_list.html"

    def get_queryset(self):
        return Vakil.objects.all()

class Riyasatlist(ListView):
    template_name = "account/riyasat_list.html"

    def get_queryset(self):
        return Riyasat.objects.all()


class vakil_image_view(View):
    def get(self, request):
        form = ImageForm()
        return render(request, 'account/vakil_image_update.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('account:vakil_list')
        return render(request, 'account/vakil_image_update.html', {'form' : form})

