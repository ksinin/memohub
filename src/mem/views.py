from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Mem

# Create your views here.

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