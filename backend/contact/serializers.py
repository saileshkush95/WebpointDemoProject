from rest_framework import serializers

from .models import ContactInfo
from django.db.models import Q


class ContactInfoModelSerializer(serializers.ModelSerializer):
    """

    NOTE: In our case model validation is sufficient,
     but in case we need custom validation still we can write those validations here
    """

    class Meta:
        model = ContactInfo
        fields = ['url', 'id', 'full_name', 'email_address', 'mobile_number']

    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        partial = getattr(self, 'partial', None)
        mobile_number = attrs.get("mobile_number")

        if partial and ContactInfo.objects.filter(Q(mobile_number=mobile_number)).exclude(id=instance.id).exists():
            raise serializers.ValidationError({"mobile_number": "Contact with this phone number already exits"})
        if not partial and ContactInfo.objects.filter(Q(mobile_number=mobile_number)).exists():
            raise serializers.ValidationError({"mobile_number": "Contact with this phone number already exits"})
        return attrs
