from django.shortcuts import render,get_object_or_404
from .models import Order

def thanks(request,order_id):
    if order_id:
        order=get_object_or_404(Order,pk=order_id)
    return render(request,'thanks.html',{'customer_order':order})
