from django.db import models


class DetailModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=False, blank=False)
    brand = models.CharField(max_length=255, verbose_name='Brand', null=False, blank=False)
    sku_code = models.CharField(max_length=255, verbose_name='SKU Code', null=False, blank=False)
    product_summary = models.TextField(verbose_name='AI Summary Description', null=False, blank=False)
    currency = models.CharField(max_length=255, verbose_name='Currency', null=False, blank=False, default='KES')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=False, blank=False)
        
    def __str__(self):
        return self.name + '-' + self.sku_code
    