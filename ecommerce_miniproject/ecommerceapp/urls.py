from django.urls import path
from . import views

app_name = 'ecommerceapp'

urlpatterns = [
    path('',views.allProdCat,name='allproducts'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodDetails,name='prodcatdetails')
]