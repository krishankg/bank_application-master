from django.urls import path

from . import views

urlpatterns=[
    path('api-list/',views.BranchInfoListApiView.as_view(),name='api'),
]