from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import OrderItem,Order
from django.template.loader import get_template
from django.core.mail import EmailMessage,send_mail


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try :
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity<cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0, cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key=settings.STRIPE_SECRET_KEY
    stripe_total=int(total*100)
    description='blabla'
    data_key=settings.STRIPE_PUBLISHABLE_KEY
    if request.method =='POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']

            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge=stripe.Charge.create(
                amount=stripe_total,
                currency='gbp',
                description=description,
                customer=customer.id
            )
            try:
                order_details=Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                )
                order_details.save()
                for order_item in cart_items :
                    oi=OrderItem.objects.create(
                        product=order_item.product.name,
                        quantity=order_item.quantity,
                        price=order_item.product.price,
                        order=order_details
                        )
                    oi.save()
            
                    products=Product.objects.get(id=order_item.product.id)
                    products.stock=int(order_item.product.stock-order_item.quantity)
                    products.save()
                    order_item.delete()
                try:
                    sendEmail(order_details.id)

                except  IOError as e:
                    return e
                return redirect('order:thanks',order_details.id)

            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return False,e
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter,data_key=data_key,stripe_total=stripe_total,description=description))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

'''google accounts dnt allow login through less secure apps so security settings of google account should be changed before sending mail'''

def sendEmail(order_id):
    transaction=Order.objects.get(id=order_id)
    order_items=OrderItem.objects.filter(order=transaction)
    try:
        subject="store new order #{}".format(transaction.id)
        to=['{}'.format(transaction.emailAddress)]
        from_email='janindur@gmail.com'
        order_information={
            'transaction':transaction,
            'order_items':order_items
        }

        message=get_template('email/email.html').render(order_information)

        msg=EmailMessage(subject,message,to=to,from_email=from_email)
        msg.content_subtype='html'
        print('ddtrdtrdrdr mail sent sahhsuahua huahua suahs uhau')
        msg.send()
        print('ddtrdtrdrdr mail sent sahhsuahua huahua suahs uhau')
    except IOError as e:
        return e
        print(e)


