from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    # path('index/', views.homeProducts, name="index"),
    path('index/', views.homeProducts, name="index"),

    path('account/', views.accountSettings, name="account"),
    path('create_Customer/', views.createCustomer, name="create_Customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]
