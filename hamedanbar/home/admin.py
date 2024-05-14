from django.contrib import admin
from .models import Article, Category, IPAddress,Vakil
from import_export.admin import ImportExportModelAdmin

from django.shortcuts import render
from .models import *
import pandas as pd
from django.http import JsonResponse
from django.conf import settings

# Admin header change
admin.site.site_header = "وبلاگ جنگویی من"

from django.shortcuts import render
from django import forms

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(Vakil)
class VakilAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'lastname', 'address', 'thumbnail_tag', 'jpublish', 'gender', 'code')
    list_filter = ('code', 'name', 'lastname')
    search_fields = ('name', 'code')
    ordering = ['code', '-date']

    def export_data_to_excel(request) :
        # Retrieve all Employee objects from the database
        objs = Vakil.objects.all()
        data = []
        for obj in objs :
            data.append({
                "code" : obj.code,
                "name" : obj.name,
                "lastname" : obj.lastname,
                "address" : obj.address,
                # "date":obj.date,
                "gender":obj.gender,

            })
        pd.DataFrame(data).to_excel('output.xlsx')
        return JsonResponse({
            'status' : 200
        })

    def import_data_to_db(request) :
        data_to_display = None
        if request.method == 'POST' :
            file = request.FILES['files']
            obj = CsvImportForm.objects.create(
                file = file
            )

            path = file.file
            df = pd.read_excel(path)
            data_to_display = df.to_html()
            print("success")

        return render(request, 'excel.html', {'data_to_display' : data_to_display})



# Register your models here.
def make_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "منتشر شد."
        else:
            message_bit = "منتشر شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
            message_bit = "پیش‌نویس شد."
        else:
            message_bit = "پیش‌نویس شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیش‌نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title','slug', 'parent','status')
	list_filter = (['status'])
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'thumbnail_tag','slug', 'author', 'jpublish','is_special', 'status', 'category_to_str')
	list_filter = ('publish','status', 'author')
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-publish']
	actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)

