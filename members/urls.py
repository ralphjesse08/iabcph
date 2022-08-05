from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

app_name = 'members'

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('', views.home, name='home'),
    path('password_change/', PasswordsChangeView.as_view(template_name='user-changepassword.html'), name = 'password_change' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
