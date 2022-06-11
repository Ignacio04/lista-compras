from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo_item', views.novo_item, name='novo_item'),
    path('edit/<int:id>', views.edit_item, name='edit_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item')
]
