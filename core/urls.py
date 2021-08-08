# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from app.views import field1, field1_predict, field2, field2_predict, field3, field4

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("api/sensors/field1", field1),
    path("api/sensors/field1/predict", field1_predict),
    path("api/sensors/field2", field2),
    path("api/sensors/field2/predict", field2_predict),
    path("api/sensors/field3", field3),
    path("api/sensors/field4", field4),
    # path("api/sensors/field2/predict", graphTempOutdoor),
    # path("api/sensors/field3", graphTempOutdoor),
    # path("api/sensors/field4", graphTempOutdoor),
    # path("api/sensors/temp", graphTemp),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
]
