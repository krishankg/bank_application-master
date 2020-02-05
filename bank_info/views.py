from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import generics,mixins
from django.shortcuts import get_object_or_404
from .models import BranchInfo
from .serializers import BranchInfoSerializer
from django.db.models import Q

from django.views.generic import ListView
from rest_framework.response import Response


class BranchListView(ListView):
	model=BranchInfo
	template_name='bank_info/bank_details.html'
	context_object_name='objects'

	def get_queryset(self):
		query=self.request.GET.get('q',None)
		queryset=BranchInfo.objects.all()
		if query is not None:
			queryset=queryset.filter(ifsc__iexact=query)
		return queryset


	# def get_context_data(self,*args,**kwargs):
	# 	context=super(BranchInfoSerializer,self).get_context_data(*args,**kwargs)




class BranchDetailsListView(ListView):
	model=BranchInfo
	template_name='bank_info/branch_details.html'
	context_object_name='objects'

	def get_queryset(self):
		bank_name=self.request.GET.get('q1',None)
		city_name=self.request.GET.get('q2',None)
		queryset=BranchInfo.objects.all()
		if bank_name is not None and city_name is not None:
			queryset=queryset.filter(Q(bank_name__iexact=bank_name),Q(city__iexact=city_name))
		return queryset
