from rest_framework import serializers
from rApi.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #fields = ('emp_id','emp_name')