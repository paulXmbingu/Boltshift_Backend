from django.db import models






class ProfileModel(models.Model):
    logo = models.ImageField(upload_to='Media/Vendors_Logos/', blank=True, null=True, verbose_name='Vendor Name')
    name = models.CharField(max_length=255, verbose_name='Vendor Name', null=False, blank=False, default='Vendor')
    star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Star Rating", null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'