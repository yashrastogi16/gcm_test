from django.contrib import admin
from forms import MemberForm4
from models import *
import autocomplete_light
# from loginapp.models import members,role

class membersInline(admin.TabularInline):
	form =  MemberForm4
	model = members
	# form = autocomplete_light.modelform_factory(members)
	# print form
	# list_display = ['user_id','username','email_id','date_time']
	# list_filter = ['date_time']
	# search_fields = ['date_time']
	# class Meta:
	# 	model = members
class membersAdmin(admin.ModelAdmin):
	form = MemberForm4
	list_display = ['username','user_id']
	inlines = [membersInline]

class roleAdmin(admin.ModelAdmin):
	list_display = ['rolename']
	class Meta:
		model = role

admin.site.register(members,membersAdmin)
admin.site.register(role,roleAdmin)
