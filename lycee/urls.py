"""mysite URL Configuration

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
from django.urls import path
from django.conf.urls import url
from .views import StudentCreateView


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^lycee/$', views.index, name='index'),
    url(r'^lycee/(?P<cursus_id>[0-9]+)$' , views.student_list, name='student_list'),
    url(r'^lycee/student/(?P<student_id>[0-9]+)$' , views.detail_student, name='detail_student'),
    url(r'^lycee/student/create/$' , StudentCreateView.as_view(), name='create_student'),
    url(r'^lycee/student/edit/(?P<student_id>[0-9]+)$' , views.edit_student, name='edit_student'),
    url(r'^lycee/cursuscall/(?P<cursus_id>[0-9]+)$' , views.cursuscall, name='cursuscall'),
    url(r'^lycee/call/' , views.particularcall, name='particularcall'),
    url(r'^lycee/presence/' , views.presence_list, name='presence_list'),
    url(r'^lycee/presence_detail/(?P<presence_id>[0-9]+)$' , views.detail_presence, name='detail_presence'),
     url(r'^lycee/student_presence/(?P<student_id>[0-9]+)$' , views.student_presence, name='student_presence'),
]
