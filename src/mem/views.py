from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DeleteView, UpdateView
from mem.forms import UserCreationForm, MemAddForm
from .models import Mem
from django.urls import reverse_lazy


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
        mems = Mem.objects.order_by('-datetime_created')
        context = {"mems": mems}
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


class YourMemView(View):
    template_name = 'yourmemes.html'

    def get(self, request):
        mems = Mem.objects.filter(user_id=request.user.id).order_by('-datetime_created')
        context = {"mems": mems}
        return render(request, self.template_name, context)


class DeleteMemView(DeleteView):
    model = Mem
    pk_url_kwarg = 'mem_id'
    success_url = reverse_lazy('yourmemes')


class EditMemView(UpdateView):
    model = Mem
    fields = ['url', 'description']
    pk_url_kwarg = 'mem_id'
    template_name = 'editmem.html'
    success_url = reverse_lazy('yourmemes')
