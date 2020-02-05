from django.contrib import admin

from .models import BranchInfo


class BranchInfoAdmin(admin.ModelAdmin):

	list_display=['branch_name','ifsc','bank_name','city','district','state','address']





admin.site.register(BranchInfo,BranchInfoAdmin)