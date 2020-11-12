from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse
# Create your views here.


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'name': profiles})


def edit(request):
    error = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form incorrect'

    form = ProfileForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'edit.html', context)


