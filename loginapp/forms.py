from django import forms
from django.forms import ModelForm,PasswordInput
from models import *
import autocomplete_light

class MemberForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = members
		fields = '__all__'
class RoleForm(forms.ModelForm):
    class Meta:
        model = role
        fields = '__all__'

class MemberForm1(forms.ModelForm):
	class Meta:
		model = members
		fields = ['id','username','gender','resident_location','contact_no']

class MemberForm2(forms.ModelForm):
	class Meta:
		model = members
		fields = ['username','gender','user_id','password','email_id','resident_location','contact_no']

class MemberForm4(forms.ModelForm):
	class Meta:
		model = members
		widgets = {
        	'tags': autocomplete_light.TextWidget('TagAutocomplete'),
       	}
		fields = '__all__'

