from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm

# Create your views here.


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# READ
@user_passes_test(lambda x: x.is_superuser)
def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


# CREATE
@user_passes_test(lambda x: x.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'form': form,
        'title': 'GeekShop - Регистрация',
        'form_class': 'col-lg-7',
        'header': 'Создание пользователя',
    }
    return render(request, 'adminapp/admin-users-create.html', context)


# UPDATE
@user_passes_test(lambda x: x.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


# DELETE
@user_passes_test(lambda x: x.is_superuser)
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))

