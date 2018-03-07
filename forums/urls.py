from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topic/add', views.topic_add, name='topic_add'),
    path(r'topic/<int:id>', views.topic_show, name='topic_show'),
    path(r'topic/edit/<int:id>', views.topic_edit, name='topic_edit'),
    path(r'topic/delete/<int:id>', views.topic_delete, name='topic_delete'),
]