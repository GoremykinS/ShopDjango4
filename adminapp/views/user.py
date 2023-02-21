
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from authapp.models import ShopUser
from django.shortcuts import render, get_object_or_404
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm



# ограничиваем вход в админку и выдаем ошибку на попытку
def check_is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True


class UserList(ListView):
    pass


@user_passes_test(check_is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)

@user_passes_test(check_is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users'))
    else:
        user_form = ShopUserRegisterForm()
    content = {'title': title, 'update_form': user_form}
    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(check_is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(check_is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)
