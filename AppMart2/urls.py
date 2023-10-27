from django.urls import path
from AppMart2 import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/<pro_name>/',views.productpage,name="productpage"),
    path('singlepro/<int:dataid>/',views.singlepro,name="singlepro"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('user_regpage/',views.user_regpage,name="user_regpage"),
    path('save_data/',views.save_data,name="save_data"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('User_Login/',views.User_Login,name="User_Login"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('save_data1/',views.save_data1,name="save_data1"),
    path('displaycart/',views.displaycart,name="displaycart"),
    path('deletecart/<int:dataid>',views.deletecart,name="deletecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('save_data3/',views.save_data3,name="save_data3"),
]