from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'post/<int:pk>',
        views.DetalhesView.as_view(),
        name='detalhes'),
    path(
        'post/add',
        views.PostCreate.as_view(),
        name='adiciona'),
    path(
        'post/<int:pk>/update',
        views.PostUpdate.as_view(),
        name='atualiza'),
    path(
        'post/<int:pk>/delete',
        views.PostDelete.as_view(),
        name='remove'),
]
