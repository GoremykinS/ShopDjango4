from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.core.paginator import Paginator


menu_links = [
    {"view_name": "index", "name": "домой"},
    {"view_name": "products_index", "name": "продукты"},
    {"view_name": "contact", "name": "контакт"},
]
# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(
        request,
        "mainapp/index.html",
        context={"message": "321", "menu_links": menu_links, "products": products},
    )


def products_index(request):

    categories = ProductCategory.objects.all()
    products = Product.objects.all()



    page = int(request.GET.get('page', default = '1'))
    per_page = int(request.GET.get('per_page', default = '3'))

    paginator = Paginator(products, per_page)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        "mainapp/products.html",
        context={
            "menu_links": menu_links,
            "categories": categories,
            "hot_product": Product.objects.hot_product,
            "products": page

        },
    )

def products(request, pk=None):

    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=selected_category).order_by('price')
    return render(
        request,
        "mainapp/products.html",
        context={
            "menu_links": menu_links,
            "selected_category": selected_category,
            "categories": categories,
            "products": products,

        },
    )


def contact(request):

    return render(request, "mainapp/contact.html", context={"menu_links": menu_links})
