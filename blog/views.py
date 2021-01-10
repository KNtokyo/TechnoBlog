from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

# from account.decorators import allowed_users
from .models import *


class Home(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все новости'
        return context

    # @admin_only
    # @login_required(login_url='login')
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def index(request):
    return render(request, 'blog/index.html')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def get_category(request, slug):
    return render(request, 'blog/category.html')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def get_post(request, slug):
    return render(request, 'blog/category.html')

