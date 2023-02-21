
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.http import HttpResponseRedirect
from adminapp.forms import EditProductForm
from django.urls import reverse

def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)

def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = EditProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('products_category', args=[pk]))
    else:
        product_form = EditProductForm(initial={'category': category})

    content = {
        'title': title,
        'update_form': product_form,
        'category': category
        }
    return render(request, 'adminapp/product_update.html', content)


def product_read(request, pk):
    title = 'продукт/подробнее'

    product = get_object_or_404(Product, pk=pk)

    content = {'title': title, 'object': product,}

    return render(request, 'adminapp/product.html', content)

def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = EditProductForm(request.POST, request.FILES, \
                                    instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('product_update', \
                                                args=[edit_product.pk]))
    else:
        edit_form = EditProductForm(instance=edit_product)

    content = {'title': title,
               'update_form': edit_form,
               'category': edit_product.category
               }
    return render(request, 'adminapp/product_update.html', content)



def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        # product.is_active = False
        # product.save()
        return HttpResponseRedirect(reverse('products_category', \
                                        args=[product.category.pk]))

    content = {'title': title, 'object': product}

    return render(request, 'adminapp/product_delete.html', content)
