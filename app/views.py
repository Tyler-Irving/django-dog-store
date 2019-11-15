from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from app.models import DogProduct, Purchase, DogTag

# Create your views here.
class ProductsListView(generic.ListView):
    model = DogProduct
    context_object_name = "dog_products"
    template_name = "home.html"

class DogProductDetailView(generic.DetailView):
    model = DogProduct
    context_object_name = "dog_product"
    template_name = "dog_product_detail.html"
    pk_url_kwarg = "dog_product_id"

class PurchaseDogProductView(generic.View):
    def post(self, request, dog_product_id):
        dog_product = DogProduct.objects.get(id=dog_product_id)
        if dog_product.quantity > 0:
            dog_product.quantity -= 1
            dog_product.save()
            purchase = Purchase.objects.create(
                dog_product=dog_product, purchased_at=timezone.now()
            )
            purchase.save()
            messages.success(request, f"Purchased {dog_product.name}")
            return redirect("purchase_detail", purchase.id)
        elif dog_product.quantity <= 0:
            messages.error(request, f"{dog_product.name} is out of stock")
            return redirect("dog_product_detail", dog_product_id)

class PurchaseDetailView(generic.DetailView):
    model = Purchase
    context_object_name = "purchase"
    template_name = "purchase_detail.html"
    pk_url_kwarg = "purchase_id"

class NewDogTagCreateView(generic.CreateView):
    model = DogTag
    fields = ["owner_name", "dog_name", "dog_birthday"]
    template_name = "new_dog_tag.html"
    success_url = reverse_lazy("dog_tag_list")
    context_object_name = "form"

class DogTagListView(generic.ListView):
    model = DogTag
    context_object_name = "dog_tags"
    template_name = "dog_tag_list.html"
