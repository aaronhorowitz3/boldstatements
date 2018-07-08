from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.statement_feed, name='statement_feed'),
    path('statements/<int:pk>/', views.statement_detail, name='statement_detail'),
    path('statements/new_statement', views.make_a_statement, name='make_a_statement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
