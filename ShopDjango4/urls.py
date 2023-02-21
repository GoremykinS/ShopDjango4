"""ShopDjango4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views
from authapp import views as authapp_views
from cartapp import views as cart_views
from adminapp import views as adminapp_views

from django.conf.urls import include

# чтобы Django раздавал медиафайлы на этапе разработки, необходимо добавить
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", mainapp_views.index, name="index"),
    path("contact/", mainapp_views.contact, name="contact"),
    path("products/", mainapp_views.products_index, name="products_index"),
    path("products/<int:pk>", mainapp_views.products, name="products"),

    path("auth/login/", authapp_views.login, name="login"),
    path("auth/logout/", authapp_views.logout, name="logout"),
    path("auth/edit/", authapp_views.edit, name="edit"),
    path("auth/register/", authapp_views.register, name="register"),

    path("cart/", cart_views.cart, name="view"),
    path("cart/add/<int:pk>", cart_views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:pk>", cart_views.remove_from_cart, name="remove_from_cart"),
    path('cart/edit/<int:pk>/<int:quantity>/', cart_views.api_edit_cart, name='edit'),



    # Debug toolbar
    path("__debug__/", include('debug_toolbar.urls')),


    path("defaultadmin/", admin.site.urls),
    # path("admin/", adminapp_views. name="admin"),


    path('admin/users/create/', adminapp_views.user_create, name='user_create'),
    path('admin/users/read/', adminapp_views.users, name='users'),
    path('users/update/<int:pk>/', adminapp_views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp_views.user_delete, name='user_delete'),
    path('categories/create/', adminapp_views.category_create, name='category_create'),
    path('categories/read/', adminapp_views.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp_views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp_views.category_delete, name='category_delete'),
    path('products/create/category/<int:pk>/', adminapp_views.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp_views.products, name='products_category'),
    path('products/read/<int:pk>/', adminapp_views.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp_views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp_views.product_delete, name='product_delete'),




]


# чтобы Django раздавал медиафайлы на этапе разработки, необходимо добавить
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
