from django.db import models

# Create your models here.
class RegisteredDevices(models.Model):
    serial_number = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    antenna_characteristics = models.TextField(blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    device_capabilities = models.TextField(blank=True, null=True)
    device_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registered_devices'


