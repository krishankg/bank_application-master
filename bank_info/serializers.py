from .models import BankInfo,BranchInfo
from rest_framework import serializers



class BankInfoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=BankInfo
		fileds=[
           'name'    
		]





class BranchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchInfo
        fields = [
            'ifsc', 'branch_name', 'bank_id', 'address',
            'city', 'district', 'state','bank_name']


