from django.db import models
from django.views.generic import *
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

class Books(models.Model):
    book_title = models.CharField(max_length=150, verbose_name = 'Knygos pavadinimas')
    publisher = models.CharField(max_length=50, verbose_name = 'Išleista (metai)')
    pages = models.CharField(max_length=10, verbose_name = 'Puslapiai')
    language = models.CharField(max_length=50, verbose_name = 'Kalba')
    book_image = models.ImageField(upload_to="images/")
    authorAdd = models.ForeignKey('BookAuthor', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.book_title
    
    class Meta:
        verbose_name = 'Knygos'
        verbose_name_plural = 'Knygos'
        ordering = ['book_title', ]

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
class BookAuthor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name = 'Autoriaus vardas, pavardė')
    country = models.CharField(max_length=50, verbose_name = 'Šalis')
    about_author = models.TextField(blank=True, verbose_name = 'Apie autorių')
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Autorius'
        verbose_name_plural = 'Autoriai'
        ordering = ['full_name', ]


# komentarų modelis
class BookReview(models.Model):
    book = models.ForeignKey('Books', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=1000)

    class Meta:
        verbose_name = 'Knygų atsiliepimai'
        verbose_name_plural = 'Knygų atsiliepimai'
