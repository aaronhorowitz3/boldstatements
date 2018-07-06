from django.urls import path
from . import views

urlpatterns = [
    path('', views.statement_feed, name='statement_feed'),
    path('statements/<int:pk>/', views.statement_detail, name='statement_detail'),
    path('statements/new_statement', views.make_a_statement, name='make_a_statement'),
]
