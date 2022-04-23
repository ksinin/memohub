from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView

from mem.forms import UserCreationForm, MemAddForm
from .models import Mem, UserFollowing


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class HomeMemView(View):
    template_name = 'home.html'

    def get(self, request):
        mems = Mem.objects.order_by('-datetime_created')
        for mem in mems:
            liked = False
            if mem.likes.filter(id=self.request.user.id).exists():
                liked = True
            mem.number_of_likes = mem.likes.count()
            mem.post_is_liked = liked
        paginator = Paginator(mems, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj
        }

        return render(request, self.template_name, context)


class YourMemView(View):
    template_name = 'yourmemes.html'

    def get(self, request, author):
        author = User.objects.get(username=author)
        author_followers = User.objects.filter(following__in=author.followers.all()).order_by(
            '-following__created_at') if author.followers.all() else []
        mems = Mem.objects.filter(user=author).order_by('-datetime_created')
        for mem in mems:
            liked = False
            if mem.likes.filter(id=self.request.user.id).exists():
                liked = True
            mem.number_of_likes = mem.likes.count()
            mem.post_is_liked = liked
        paginator = Paginator(mems, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj,
            "author": author,
            "author_followers": author_followers,
            "author_followers_count": author.followers.count(),
            "author_following_count": author.following.count()
        }
        return render(request, self.template_name, context)


class AddMemView(View):
    template_name = 'addmem.html'

    def get(self, request):
        form = MemAddForm()
        return render(request, self.template_name, {'form': form, 'title': 'Add mem'})

    def post(self, request):
        form = MemAddForm(request.POST)
        if form.is_valid():
            mem = form.save(commit=False)
            mem.user = request.user
            mem.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form, 'title': 'Add mem'})


class DeleteMemView(DeleteView):
    model = Mem
    pk_url_kwarg = 'mem_id'

    def get_success_url(self):
        return reverse_lazy('yourmemes', kwargs={'author': self.request.user})


class EditMemView(UpdateView):
    model = Mem
    fields = ['url', 'description']
    pk_url_kwarg = 'mem_id'
    template_name = 'editmem.html'

    def get_success_url(self):
        return reverse_lazy('yourmemes', kwargs={'author': self.request.user})


class UserFollowingView(View):
    template_name = 'user_following_followers_list.html'

    def get(self, request, author):
        author = User.objects.get(username=author)
        author_followers = author.following.all()
        following = User.objects.filter(followers__in=author_followers).order_by('-followers__created_at') if author_followers else []
        paginator = Paginator(following, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "author": author
        }
        return render(request, self.template_name, context)


class UserFollowersView(View):
    template_name = 'user_following_followers_list.html'

    def get(self, request, author):
        author = User.objects.get(username=author)
        author_following = author.followers.all()
        followers = User.objects.filter(following__in=author_following).order_by('-following__created_at') if author_following else []
        paginator = Paginator(followers, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "author": author
        }
        return render(request, self.template_name, context)


class FollowToggleUserView(UpdateView):

    def post(self, request, author):
        author = User.objects.get(username=author)
        current_user = request.user
        author_following = author.followers.all()
        followers = User.objects.filter(following__in=author_following) if author_following else []

        if author != current_user:
            if current_user in followers:
                UserFollowing.objects.filter(user=current_user, following_user=author).delete()
            else:
                UserFollowing.objects.create(user=current_user, following_user=author)

        return redirect(reverse_lazy('yourmemes', kwargs={'author': author}))


class MemLikeView(UpdateView):

    def post(self, request, mem_id):
        mem = get_object_or_404(Mem, id=mem_id)
        if mem.likes.filter(id=request.user.id).exists():
            mem.likes.remove(request.user)
        else:
            mem.likes.add(request.user)
        return HttpResponseRedirect(reverse('home'))
