from django.urls import path

from todoapp import views

urlpatterns=[
    path('',views.todo,name='todo'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('viewtodo',views.viewtodo,name='viewtodo'),
    path('update_todo/<int:id>/',views.update_todo,name='update_todo'),
    path('de_todo/<int:id>/',views.del_todo,name='del_todo')
]
