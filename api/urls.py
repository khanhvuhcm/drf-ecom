from django.urls import path, include

# from rest_framework.authtoken import views

from api import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('accounts/', include('api.accounts.urls')),
    path('cart/', include('api.cart.urls')),
    path('profiles/', include('api.billing.urls')),
]