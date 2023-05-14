from rest_framework import routers

from .viewsets import ContactInfoViewset

router = routers.DefaultRouter()
router.register("contact-info", ContactInfoViewset)
