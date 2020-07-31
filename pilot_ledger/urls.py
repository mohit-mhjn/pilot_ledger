
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('authenticate/', views.authenticate, name="loginauth"),
    path('signup/', views.signup, name="signup_form"),
    path('postsignup/', views.postsignup, name="postsignup"),
    #path('dashboard/', include('dashboard.urls')),
]