from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import UserProfile
from rest_framework import exceptions
from django.conf import settings


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        user_profile = UserProfile.objects.get(user_id=self.user.id)
        if user_profile.status == 'PENDING':
            error_message = "Not an active user, status is pending"
            raise exceptions.AuthenticationFailed(error_message)
        data.update({'id': self.user.id})
        data.update({'email': self.user.email})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'role': user_profile.role})
        data.update({'access_expiry_in_sec': (settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])})
        data.update({'refresh_expiry_in_sec': (settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'])})
        return data
