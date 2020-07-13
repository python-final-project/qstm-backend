from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name="user_list"),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    path('parents/', ParentListView.as_view(), name="parent_list"),
    path('parents/<int:pk>/', ParentDetailView.as_view(), name='parent_detail'),

    path('students/', StudentListView.as_view(), name="student_list"),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

    path('sites/', SiteListView.as_view(), name="site_list"),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site_detail'),
]