"""dog_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.ProductsListView.as_view(), name="home"),
    path(
        "dog-product/<dog_product_id>",
        app.views.DogProductDetailView.as_view(),
        name="dog_product_detail",
    ),
    path(
        "dog-product/<dog_product_id>/purchase",
        app.views.PurchaseDogProductView.as_view(),
        name="purchase_dog_product",
    ),
    path(
        "purchase/<purchase_id>",
        app.views.PurchaseDetailView.as_view(),
        name="purchase_detail",
    ),
    path("dogtag/new", app.views.NewDogTagCreateView.as_view(), name="new_dog_tag"),
    path("dogtag", app.views.DogTagListView.as_view(), name="dog_tag_list"),
]
