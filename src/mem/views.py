from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from mem.forms import UserCreationForm
from .models import Mem


class Register(View):

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
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)


@login_required(login_url="login/")
def main_view(request):
    if request.method == "GET":
        mems = Mem.objects.filter(user_id=request.user.id)
        return render(
            request,
            "../templates/main.html",
            {"mems": mems, "username": request.user.username}
        )

    return ""