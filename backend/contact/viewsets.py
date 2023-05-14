from rest_framework import viewsets

from .models import ContactInfo
from .serializers import ContactInfoModelSerializer


class ContactInfoViewset(viewsets.ModelViewSet):
    """
    I'm using model viewset but we can use function based or
    class based it depends on requirements but i prefer viewset
    because it help to manage code readablilyt
    """
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoModelSerializer
    search_fields = ["full_name"]
