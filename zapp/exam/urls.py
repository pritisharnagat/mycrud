from django.contrib import admin
from django.urls import path,include
from exam import views
urlpatterns = [
    path("exam",views.exam,name="exam"),
    path("",views.myexam,name="myexam"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    path("update/updaterecord/<int:id>",views.updaterecord,name="updaterecord"),
]    
