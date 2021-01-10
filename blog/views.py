from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# @login_required(login_url='login')
class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все новости'
        return context

@login_required(login_url='login')
def index(request):
    return render(request, 'blog/index.html')

@login_required(login_url='login')
def get_category(request, slug):
    return render(request, 'blog/category.html')

@login_required(login_url='login')
def get_post(request, slug):
    return render(request, 'blog/category.html')

