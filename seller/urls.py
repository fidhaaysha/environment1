from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns=[
    path('home', views.seller_home,name='path1'),
    path('product',views.add_product,name='path2'),
    path('masterpage',views.master,name='path3'),
]