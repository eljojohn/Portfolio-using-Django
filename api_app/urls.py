from django.urls import path
from . import views

urlpatterns = [

    path('projects/', views.api_projects),

    path('projects/<slug:slug>/', views.api_project_detail),

    path('projects/create/', views.api_project_create),

    path('contact/', views.api_contact_create),

]
