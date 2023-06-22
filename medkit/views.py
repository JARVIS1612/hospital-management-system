from datetime import datetime
import random
from django.shortcuts import render, redirect
from authentication.models import Users
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from .models import Orders


# Create your views here.

def order(request):
    success = ""
    if request.method == "POST":
        img = request.FILES['img']
        fs = FileSystemStorage()
        fileurl = fs.save(img.name, img)
        filepath = fs.url(fileurl)
        print(filepath)
        order = Orders(username=Users(username=request.user), prescription=filepath)
        order.save()
        success = "Your Order is Placed"
    return render(request, 'medkit/order.html', {'success': success})

def taken(r, order_id, taken):
    order = Orders.objects.get(id=order_id)
    order.is_taken = (taken=="taken")
    order.save()
    return redirect("order_dashboard")

def Dashboard(request, order_id=0):
    orders = Orders.objects.filter(is_ready=False, is_taken=False)
    print(orders)
    if request.method == "POST":
        if order_id != 0:
            cost = request.POST['cost']
            order = Orders.objects.get(id=order_id)
            order.is_ready = True
            order.cost = cost
            order.uniquecode = random.randint(10000,99999)
            order.save()
            return redirect("order_dashboard")
        elif order_id == 0:
            is_ready = request.POST.get('is_ready', False)
            is_taken = request.POST.get('is_taken', False)
            if is_ready or is_taken:
                if is_ready and not is_taken:
                    orders = Orders.objects.filter(is_ready=True, is_taken=False)
                if is_taken:
                    orders = Orders.objects.filter(is_taken=True)

    return render(request, 'medkit/dashboard.html', {"orders": orders})
