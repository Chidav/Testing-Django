from django.shortcuts import render
from .models import gallery, Contact, pricing
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

def post_detail(request, price):
    if price > 0:
        prices = pricing(price1=price)
        prices.save()
        messages.success(request, 'Purchase Successful, thank you')
        return redirect('onlinecourseapp:home')
    all_gallery = gallery.objects.all()

    context = {
        "all_gallery": all_gallery
    }

    return render(request, 'onlinecourseapp/index.html', context)


def home(request):
    all_gallery = gallery.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contacts = Contact(name=name, phone=phone, email=email, message=message)
        contacts.save()
        messages.success(request, 'Message saved successfully, thank you')

    context = {
        "all_gallery": all_gallery
    }

    return render(request, 'onlinecourseapp/index.html', context)
