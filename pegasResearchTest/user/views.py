from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
from django.views.generic import ListView


from .forms import (UserCreationForm, PasswordChangeForm)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    ordering = ['username']


@login_required
def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('user-list')
    else:
        form = UserCreationForm()
    return render(request, 'user/form.html', { 'form': form })


@login_required
def update(request, **kwargs):
    user = get_object_or_404(User, pk=kwargs['pk'] )
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Password changed for {user.username} account.')
            return redirect('user-list')
    else:
        form = PasswordChangeForm(user=user)
    return render(request, 'user/form.html', { 'form': form })


@login_required
def profile(request):
    return render(request, 'user/profile.html')
