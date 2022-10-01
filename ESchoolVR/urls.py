from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.loginPage,name="login"),
    path('edit/',views.editProfile,name="edit"),
    path('user/',views.userPage,name="user"),
    path('chat/',views.chatPage,name="chat"),
    path('starter/',views.starterPage,name="starter"),
    path('help/',views.helpPage,name="help"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('', views.courses, name="courses"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/',views.updateItem, name="update_item"),
]