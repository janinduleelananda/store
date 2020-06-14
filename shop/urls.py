from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

app_name='shop'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='ProdCatDetail'),
    path('account/create',views.signupView,name='signup'),
    path('account/login',auth_views.LoginView.as_view(template_name='accounts/signin.html'),name='signin'),
    path('account/logout',views.signoutView,name='signout'),
]
