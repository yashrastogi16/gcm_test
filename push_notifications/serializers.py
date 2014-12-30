from django.forms import widgets
from rest_framework import serializers
from models import *

# GCM Device serializers
class GCMDeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = GCMDevice
		fields = ('name','registration_id')