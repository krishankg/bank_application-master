from django.urls import path

from . import views


urlpatterns=[
    path('',views.BranchListView.as_view(),name='api_list'),
    path('api-details/',views.BranchDetailsListView.as_view(),name='api_details'),
]