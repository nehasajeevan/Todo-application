from django.urls import path
from .views import index,toggle_task,delete_task,update_task

urlpatterns=[
    path('',index,name='index'),
    path('toggle_task/<int:id>/',toggle_task,name='toggle_task'),
    path('delete_task/<int:id>/',delete_task,name='delete_task'),
    path('update_task/<int:id>/',update_task,name='update_task')
]