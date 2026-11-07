from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('footer/',views.footer,name='footer'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'
    ),
]
