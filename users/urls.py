from django.urls import path
from .views import UserList, UserDetail, TaskList, TaskListDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>', TaskListDetail.as_view())
]
