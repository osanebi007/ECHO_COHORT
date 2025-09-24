"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myproject import views
from django.urls import include # Import include function
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.sayHello),
    path('getmessage/', views.get_todos),
    path('postmessage/', views.post_todo),
    path('clubnames/', views.clubNames),
    path('updatemessage/<int:index>/', views.update_todo),
    path('deletemessage/<int:index>/', views.delete_todo),
    path('department/', include('department.urls')),
    path('inventory/', include('inventory.urls')),
]
