from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView

from images_app.forms import AddCardForm
from images_app.models import Card, Rarity, CardType, Image


# class Index(ListView):
#     template_name = "index.html"
#     model = Card

def index_view(request):
    cards = Card.objects.all().order_by('pk')
    raritys = Rarity.objects.all()
    card_type = CardType.objects.all()

    return render(request, "index.html", {
        "cards": cards,
        "raritys": raritys,
        "card_type": card_type,
    })


def signup_view(request):
    error = ""
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("images_app:index")
        else:
            error = form.errors
            print(error)
    else:
        form = UserCreationForm()
    return render(request, "../templates/sign_up.html", {
        "form": form,
        "errormsg": error
    })


def signin_view(request):
    error = ""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect("images_app:index")
    else:
        form = AuthenticationForm()
    return render(request, "../templates/sign_up.html", {
        "form": form,
        "errormsg": error
    })


def logout_view(request):
    logout(request)
    return redirect('images_app:index')


# class AddCardView(CreateView):
#     model = Card
#     form_class = AddCardForm
#     template_name = "index.html"
#     success_url = "images_app:index"

def add_card(request):
    if request.method == "POST":
        user = request.user

        if user.is_superuser:
            images = request.FILES.getlist("images")
            print("IMAGE: ", images)
            card_name = request.POST.get("card_name")
            rarity_request = request.POST.get("rarity")
            card_type_request = request.POST.get("card_type")


            rarity = Rarity.objects.get(rarity__exact=rarity_request)
            card_type = CardType.objects.get(card_type__exact=card_type_request)

            new_card = Card(card=card_name, rarity=rarity, card_type=card_type)
            new_card.save()

            card = Card.objects.get(card__exact=card_name)

            if not images:
                pass
            else:
                for image in images:
                    new_image = Image(card=card, photo=image)
                    new_image.save()



            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/?error=not_authenticated')

    else:
        return HttpResponseRedirect('/')


def card_detail_view(request, pk):
    card = Card.objects.get(pk=pk)
    print(type(card.rarity))

    return render(request, 'card_detail.html', {
        "card": card,
    })

# def add_photo(request):
#
#     if request.method == "POST":
#         data = request.POST
#         images = request.FILES.get("images")
