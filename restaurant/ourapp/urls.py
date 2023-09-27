from django.urls import path
from ourapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('productpage/<slug>',views.productpage,name="productpage"),
    path('searching',views.searching,name="searching"),
    path('pagination',views.pagination,name="pagination")
]
