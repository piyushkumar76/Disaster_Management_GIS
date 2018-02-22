from rest_framework import serializers
from . models import Request, ControlCenterLogIN

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'




class ControlCenterLogINSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlCenterLogIN
        fields = '__all__'



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_Request
#         fields = '__all__'
