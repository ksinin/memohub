from django.shortcuts import render
from .models import Mem
from django.contrib.auth import logout
from django.shortcuts import redirect

def main_view(request):
    template = "../templates/main.html"
    context = {
        "is_authenticated": False
    }
    if request.user.is_authenticated:
        mems = Mem.objects.filter(user_id=request.user.id)
        context = {
            "mems": mems,
            "username": request.user.username,
            "is_authenticated": True,
        }
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('main')