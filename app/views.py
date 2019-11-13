from django.shortcuts import render, redirect
from django.utils import timezone
from app.models import DogProduct, Purchase, DogTag
from app.forms import NewDogTagForm

# Create your views here.
def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_dog_product(request):
    pass


def purchase_detail(request):
    pass


def new_dog_tag(request):
    pass


def dog_tag_list(request):
    pass
