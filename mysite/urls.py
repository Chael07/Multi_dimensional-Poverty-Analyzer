"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from interface.views import(
    home_screen_view, privacy_screen_view, evaluation_screen_view, submit_household, result_screen_view, login_acc, user_login_view
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login_view, name='userlogin'),
    path('home/', home_screen_view, name='home'),
    path('privacy/', privacy_screen_view, name='privacy'),
    path('evaluations/', evaluation_screen_view, name='eval'),
    path('result/', result_screen_view, name='result'),
    # path('submit_contact_form/', submit_contact_form, name='submit_contact_form'),
    path('submit_household/', submit_household, name='submit_household'),
    path('login/', login_acc, name='loginAcc'),
    path('', include('interface.urls')),  # Include your app's URLs
    
]
