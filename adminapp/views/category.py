
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import ProductCategory
from django.core.exceptions import PermissionDenied
from adminapp.forms import CategoryEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse




def check_is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True



@user_passes_test(check_is_superuser)
def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)

def category_create(request):
    title = 'категория/создание'

    if request.method == 'POST':
        category_form = CategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('categories'))
    else:
        category_form = CategoryEditForm()
    content = {'title': title, 'update_form': category_form}
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(check_is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = CategoryEditForm(request.POST, request.FILES, instance=edit_category)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('category_update', args=[edit_category.pk]))
    else:
        edit_form = CategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)








def category_delete(request, pk):
    title = 'категория/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.delete()
        # вместо удаления лучше сделаем неактивным
        # category.is_active = False
        # category.save()
        return HttpResponseRedirect(reverse('categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)

