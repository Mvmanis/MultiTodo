from django.contrib import admin
from django.urls import path
from app.views import home,login,signup,add_todo,signout,delete_todo,change_status




urlpatterns = [
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('signup/',signup),
    path('add-todo/',add_todo),
    path('logout/',signout),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_status),
    
]
