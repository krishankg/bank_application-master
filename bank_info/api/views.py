from bank_info.models import BranchInfo
from bank_info.serializers import BranchInfoSerializer

from rest_framework.generics import ListAPIView


class BranchInfoListApiView(ListAPIView):

	serializer_class=BranchInfoSerializer


	def get_queryset(self,*args,**kwargs):

		queryset_list=BranchInfo.objects.all()
		query=self.request.GET.get('q',None)
		if query is not None:
			queryset_list=queryset_list.filter(ifsc_iexact=query)

		return queryset_list