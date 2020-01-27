from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
from django.views.generic import (
    ListView,
    DeleteView
)
from .forms import (
    UserCreationForm,
    PasswordChangeForm
)


#
# List of users view
#
class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    ordering = ['username']

    # PermissionRequiredMixin settings
    permission_required = 'auth.add_user'


#
# User creation view
#
@login_required
@permission_required('auth.add_user', login_url='/')
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


#
# User's password update view
#
@login_required
@permission_required('auth.add_user', login_url='/')
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


#
# Delete user view
#
class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'user/confirm_delete.html'
    success_url = '/user/'

    # PermissionRequiredMixin settings
    permission_required = 'auth.delete_user'
