"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# 폴더명(= 패키지)  파일명(= 모듈)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 접두사가 'myapp/'이면, myapp.urls로 던지겠다
    path('myapp/', include('myapp.urls')),

    # 접두사가 'hair/'면, hair/urls.py로 던지겠다. 
    path('hair/', include('hair.urls')),

    # 접두사가 'yourapp/'면, yourapp/urls.py로 던지겠다. 
    path('yourapp/', include('yourapp.urls')),

    # 접두사가 'utilities/'면, utilities/urls.py로 던지겠다. 
    path('utilities/', include('utilities.urls')),

]
