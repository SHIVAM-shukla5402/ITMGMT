from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('', indexView),
   # path('update', UserForm),
]

admin.site.site_header = "Software and Hardware Maintenance Admin"
admin.site.site_title = "Software and Hardware Maintenance Admin Portal"
admin.site.index_title = "Welcome to IT MGMT Portal"