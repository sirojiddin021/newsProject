from rest_framework import serializers
import news.models as models


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data['password']
        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user