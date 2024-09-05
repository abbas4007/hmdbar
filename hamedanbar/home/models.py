from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
# from comment.models import Comment

# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی‌پی")


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی",blank=True,null=True)
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),		 # draft
        ('p', "منتشر شده"),		 # publish
        ('i', "در حال بررسی"),	 # investigation
        ('b', "برگشت داده شده"), # back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articless', verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="image", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    # comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name="hits", verbose_name="بازدیدها")
    video = models.FileField(blank = True,null = True,verbose_name= 'وید‍‍یو')
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته‌بندی"

    objects = ArticleManager()

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'articleimages/',blank=True, null=True)

    def __str__(self):
        return self.article.title

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Vakil(models.Model):
    GENDER_CHOICES = (
        ('M', 'مرد'),
        ('F', "زن"),

    )
    name = models.CharField(max_length=100, verbose_name="نام" ,blank = True,null = True)
    code = models.IntegerField( blank = True,null = True,verbose_name="شماره پروانه")
    gender = models.CharField(blank = True,null = True,max_length=1, choices=GENDER_CHOICES, verbose_name="جنسیت")
    date = models.DateTimeField(blank = True,null = True, verbose_name="تاریخ انقضا")
    lastname = models.CharField( blank = True,null = True,max_length = 150,verbose_name="نام خانوادگی")
    address = models.TextField(blank = True,null = True,verbose_name="آدرس")
    thumbnail = models.ImageField(upload_to="images", verbose_name= "تصویر وکیل",blank = True,null = True)
    city = models.CharField(max_length = 150,blank = True,null = True,verbose_name = 'شهر')

    def __str__(self):
        return str(self.name)



    def jpublish(self):
        return jalali_converter(self.date)
    jpublish.short_description = "تاریخ انقضا"

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"

class Riyasat(models.Model):
    vakil = models.ForeignKey(Vakil,on_delete = models.CASCADE,related_name = 'vakils',verbose_name = 'وکیل' ,blank = True,null = True)
    role  = models.CharField(max_length = 50,verbose_name = 'نقش',unique = True)

    def __str__(self):
        return str(self.vakil)


class Comision(models.Model):
    name = models.CharField(max_length = 150,unique = True)
    aaza = models.ForeignKey(Vakil,on_delete = models.CASCADE,blank = True,null = True)
    raees = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class  ComisionVarzeshi(models.Model):
    aaza = models.ForeignKey(Vakil,on_delete = models.CASCADE,blank = True,null = True,related_name = 'aazas')
    raees = models.BooleanField(default = False)

    def __str__(self):
        return self.aaza.name