from django.urls import path
from AppMart import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="index.html"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savedata/',views.savedata,name="savedata"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('savedata2/',views.savedata2,name="savedata2"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('adminlogin/',views.adminlogin,name="Adminlogin.html"),
    path('adminlogpage/',views.adminlogpage,name="adminlogpage"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
]