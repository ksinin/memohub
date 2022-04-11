from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from mem.forms import UserCreationForm
from .models import Mem


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
        context = {'form': form}
        return render(request, self.template_name, context)


class HomeMemView(View):
    template_name = 'home.html'

    def get(self, request):
        mems = Mem.objects.filter(user_id=request.user.id)
        context = {
            "mems": mems
        }
        return render(request, self.template_name, context)
