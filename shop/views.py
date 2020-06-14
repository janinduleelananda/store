from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.models import User,Group
from .forms import SignUpForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import AuthenticationForm

def index(requset):
    text_var='this is my first django app webapage'
    return HttpResponse(text_var)
#category view
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!= None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)

    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage, InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'shop/category.html',{'category':c_page,'products':products})

def ProdCatDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'shop/product.html',{'product':product})

def signupView(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user=User.objects.get(username=username)
            customer_group=Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)

    else:
        form=SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:allProdCat')
            else:
                return redirect('shop:signup')
    else:
        form=AuthenticationForm()
        return render(request,'accounts/signin.html',{'form':form})