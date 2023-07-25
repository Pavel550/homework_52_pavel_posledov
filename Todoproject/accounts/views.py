from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import ProjectUserCreationForm


# Create your views here.
def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            next = request.GET.get("next")
            if next:
                return redirect(next)
            return redirect('webapp:home')
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context = context)



def logout_view(request):
    logout(request)
    return redirect('webapp:home')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProjectUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:home')
    else:
        form = ProjectUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})