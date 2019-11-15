from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from app.models import DogProduct, Purchase, DogTag
from app.forms import NewDogTagForm

# Create your views here.
class ProductsView(generic.ListView):
    # Class based list view for the home.html page that displays all of the products on the webpage
    # USED FOR THE PROJECT IN ITS CURRENT STATE | NOT REQUIRED TO FINISH THE PROJECT(EXTRA)
    model = DogProduct
    context_object_name = "dog_products"
    template_name = "home.html"

class DogProductDetailView(generic.DetailView):
    # class based detail view for the dog_product_detail.html page that displays the details about the desired product
    # USED FOR THE PROJECT IN ITS CURRENT STATE | NOT REQUIRED TO FINISH THE PROJECT(EXTRA)
    model = DogProduct
    context_object_name = "dog_product"
    template_name = "dog_product_detail.html"
    pk_url_kwarg = "dog_product_id"

def purchase_dog_product(request, dog_product_id):
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


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def new_dog_tag(request):
    if request.method == "GET":
        return render(request, "new_dog_tag.html")
    elif request.method == "POST":
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            DogTag.objects.create(
                owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday
            )
            return redirect("dog_tag_list")
        else:
            return render("new_dog_tag.html", {"form": form})


def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})
