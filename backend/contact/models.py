from django.db import models

from .utils import validate_mobile_number


class ContactInfo(models.Model):
    # NOTE: we can extend this class from other class to track timestamp and other info
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=255, validators=[validate_mobile_number])

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Infos"
        db_table = "contact_name"

    def __str__(self):
        return self.full_name
