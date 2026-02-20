from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # ADD first
    path('add/', views.project_add, name='project_add'),

    # EDIT
    path('edit/<slug:slug>/', views.project_edit, name='project_edit'),

    # DELETE
    path('delete/<slug:slug>/', views.project_delete, name='project_delete'),

    # LIST
    path('', views.project_list, name='projects'),

    # DETAIL MUST BE LAST
    path('<slug:slug>/', views.project_detail, name='project_detail'),



]
