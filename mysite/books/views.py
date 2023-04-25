
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *
from django.views import generic
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.db.models import Q
from django.views import*
from django.views.generic import *
from .forms import BookReviewForm
from django.views.generic.edit import FormMixin
from django.urls import reverse

# Create your views here.

menu = [{'title': "Pradžia", 'url_name': "index"},
        {'title': "Knygų rekomendacijos", 'url_name': "info"},
        {'title': "Autoriai", 'url_name': "authors"}
]

# pagrindinis puslapis
def index(request):
    books_count = Books.objects.count()
    book_author_count = BookAuthor.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'menu': menu,  
        'title': 'Rekomenduokite knygą!',
        'books_count': books_count,
        'book_author_count': book_author_count,
        'num_visits': num_visits
    }
    return render(request, 'books/index.html', context=context)

# knygų informacijos puslapis (Rekomenduotinų knygų psl.)
def info(request):
    allbooks = Books.objects.all()
    context = {
        'allbooks': allbooks,
        'menu': menu,        
        'title': 'Knygų sąrašas',
        'title2': 'Rekomenduotinų knygų sąrašas'
    }
    return render(request, 'books/info.html', context=context)

# apie autorius
def authors(request):
    allauthors = BookAuthor.objects.all()
    context = {
        'allauthors': allauthors,
        'menu': menu,        
        'title': 'Knygų autoriai',
        'title2': 'Apie knygų autorius'
    }
    return render(request, 'books/authors.html', context=context)

# prisijungimas
def login(request):
    context = {
        'menu': menu,        
        'title': 'Prisijungimas',
    }
    return render(request, 'books/registration/login.html', context=context)

# atsijungimas
def logged_out(request):
    context = {
        'menu': menu,        
        'title': 'Atsijungti',
    }
    return render(request, 'books/logged_out.html', context=context)

# slaptažodžio atstatymas
def password_reset(request):
    context = {
        'menu': menu,        
    }
    return render(request, 'books/password_reset_form.html', context=context)


# vartotojo registracija
@csrf_protect
def register(request):
    context = {
        'menu': menu,        
        'title': 'Registracija',
    }
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
        messages.error(request, f'Vartotojas užregistruotas! Galite prisijungti.')
    return render(request, 'books/register.html', context=context)

# paieška
def search(request):
    query = request.GET.get('query')
    search_results = Books.objects.filter(Q(book_title__icontains=query) | Q(language__icontains=query))
    return render(request, 'books/search.html', {'books': search_results, 'query': query})

# atsiliepimai
class BookDetailView(FormMixin, generic.DetailView):
    model = Books
    template_name = '/books/info.html'
    form_class = BookReviewForm

    class Meta:
        ordering = ['book_title']

    def get_success_url(self):
        return reverse('books/info', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.book = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(BookDetailView, self).form_valid(form)
    
