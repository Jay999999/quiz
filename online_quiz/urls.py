"""online_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from quiz.views import quiz_page, home, login_page, logout_page
from quiz.urls import quiz_router

urlpatterns = [
    path('', home, name="home"),
    path('add_quiz/', quiz_page, name="addQuestion"),
    path('admin/', admin.site.urls),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
]

urlpatterns += [
    path('quiz/', include(quiz_router.urls))
]