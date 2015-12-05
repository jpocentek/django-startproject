from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^change-password/', auth_views.password_change, {
        'template_name': 'registration/password_change.html',
        'post_change_redirect': '/'}, name="password-change"),
    url(r'^login/', views.LoginView.as_view(), name="login"),
    url(r'^logout/', auth_views.logout, {'next_page': '/accounts/login/'}, name="logout"),
    url(r'^register/', views.RegisterView.as_view(), name="register"),
    url(r'^$', views.ProfileUpdateView.as_view(), name="profile"),
]
