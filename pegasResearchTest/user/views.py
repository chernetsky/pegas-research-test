from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import UserCreationForm


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'
    ordering = ['username']
    


def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('data-home')
    else:
        form = UserCreationForm()
    return render(request, 'user/create.html', { 'form': form })


@login_required
def profile(request):
    return render(request, 'user/profile.html')
