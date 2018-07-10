from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', views.statement_feed, name='statement_feed'),
    path('statements/<int:pk>/', views.statement_detail, name='statement_detail'),
    path('statements/<int:pk>/statement_edit', views.statement_edit, name='statement_edit'),
    path('statements/new_statement', views.make_a_statement, name='make_a_statement'),
    path('statements/', include('django.contrib.auth.urls')),
    path('statements/login/', views.login_user, name='login_user'),
    path('statements/logout/', views.logout_user, name='logout_user'),
    path('statements/signup/', views.signup_user, name='signup_user'),
    path('auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
