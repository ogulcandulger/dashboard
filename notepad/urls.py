from django.urls import path
from . import views
from .views import NoteList

app_name = 'notepad'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_view, name='create'),
    path('delete/', views.delete_view, name='delete'),
    path('<id>/update/', views.update_view, name='update'),
    path('list/', NoteList.as_view(), name='list'),
    path('<id>/delete/', views.delete_view, name='delete'),

]
