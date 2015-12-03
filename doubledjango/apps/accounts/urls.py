from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.ProfileUpdateView.as_view(), name="profile"),
]
