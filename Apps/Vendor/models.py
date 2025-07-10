from django.db import models






class ProfileModel(models.Model):
    logo = models.ImageField(upload_to='Media/Vendors_Logos/', blank=True, null=True, verbose_name='Vendor Name')
    name = models.CharField(max_length=255, verbose_name='Vendor Name', null=False, blank=False)

    class Meta:
        verbose_name = 'Profile Model'
        verbose_name_plural = 'Profile Models'