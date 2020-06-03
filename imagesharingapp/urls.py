"""imagesharingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from imagesharingapp import views
from django.views.static import serve



urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('register/', views.register, name='register'),
    path('posts/', include('imageapi.urls', namespace='posts'))
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
