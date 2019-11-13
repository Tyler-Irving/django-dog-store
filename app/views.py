from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from app.models import DogProduct, Purchase, DogTag
from app.forms import NewDogTagForm

# Create your views here.
def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    if dog_product.quantity > 0:
        dog_product.quantity -= 1
        purchase = Purchase.objects.create(
            dog_product=dog_product, purchased_at=timezone.now()
        )
        return redirect("purchase_detail.html", purchase.id)
    elif dog_product.quantity <= 0:
        messages.error(f"{dog_product.name} is out of stock")
        return redirect("dog_product_detail.html", dog_product_id)



def purchase_detail(request):

def new_dog_tag(request):
    pass


def dog_tag_list(request):
    pass
