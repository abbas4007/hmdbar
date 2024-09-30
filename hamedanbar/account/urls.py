from django.contrib.auth import views
from django.urls import path
from .views import (
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    AddVakil,
    vakileList,
    Riyasatlist,
# vakil_image_view,
)

app_name = 'account'

urlpatterns = [
	path('', ArticleList.as_view(), name="home"),
	path('vakillist', vakileList.as_view(), name="vakil_list"),
	path('riyasatlist', Riyasatlist.as_view(), name="riyasat_list"),
	path('addvakil', AddVakil.as_view(), name="vakil_add"),
    path('article/create', ArticleCreate.as_view(), name="article_create"),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name="article_update"),
	path('article/delete/<int:pk>', ArticleDelete.as_view(), name="article_delete"),
    # path('image_upload', vakil_image_view.as_view(), name = 'image_upload'),

]
