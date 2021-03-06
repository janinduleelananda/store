from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__icontains=query.lower()) | Q(description__icontains=query.lower()))
    return render(request,'search.html',{'products':products,'query':query})    