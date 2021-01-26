from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.views.generic.base import View

from .forms import SignupForm
from .models import Post, Book


# from django.core.paginator import Paginator


class PostView(ListView):
    template_name = 'post/index.html'
    paginate_by = 3
    model = Post
    context_object_name = 'posts'

    # queryset = Post.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        return context


class RegisterView(View):
    template_name = 'post/register.html'

    def get(self, request):
        form = SignupForm()
        return render(request, 'post/register.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect(reverse('login'))
        else:
            print(form.error_messages)
            return render(request, 'post/register.html', {'form': form,
                                                          'errors': form.error_messages})


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['search'] = Book.objects.filter(title__icontains=self.request.POST.get('search', ''))
            context['zapros'] = self.request.POST.get('search', '')
            context['count'] = Book.objects.filter(title__icontains=self.request.POST.get('search', '')).count()
        else:
            context['search'] = Book.objects.all()
        return context

    def post(self, request):
        return render(request, self.template_name, self.get_context_data())


class PostCreateView(CreateView):
    template_name = 'post/add.html'
    model = Post
    fields = '__all__'
    success_url = '/'  # Успешный путь


class PostUpdateView(UpdateView):
    template_name = 'post/post_update.html'
    model = Post
    fields = '__all__'
    success_url = '/'  # Успешный путь


class PostDraftView(TemplateView):
    template_name = 'post/draft.html'

    def get_context_data(self, **kwargs):
        context = super(PostDraftView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class UserDetailView(DetailView):
    template_name = 'post/user_detail.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self['pk'])
        context['users'] = Post.objects.filter(user__title=user)
        return context
