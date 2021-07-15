# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from app.views import graphTempOutdoor, graphTemp 

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("api/sensors/temp_outdoor", graphTempOutdoor),
    path("api/sensors/temp", graphTemp),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
]
