from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path("",views.index),
    path("signin",views.signin),
    path("signup",views.signup),
    path("dashboard",views.dashboard),
    path("viewstudents",views.viewstudents),
    path("lgout",views.lgout),
    path("course",views.course),
    path("addcourses",views.addcourses),
    path('deletecourse',views.deletecourse),
    path('updatecourse',views.updatecourse),
    path('searchcourse',views.searchcourse),
    path('addstudent',views.addstudent),
    path('deletestudent',views.deletestudent),
    path('updatestudent/<int:pk>',views.updatestudent,name="update"),
    path('searchstudent',views.searchstudent),
    path('teacher',views.showTeacher),
    path('addteacher',views.addteacher,name="addTeacher")
]

