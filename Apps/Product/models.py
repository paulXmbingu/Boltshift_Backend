from django.db import models



''' DETAIL MODEL'''
class DetailModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=False, blank=False)
    brand = models.CharField(max_length=255, verbose_name='Brand', null=False, blank=False)
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='products', null=True, blank=False)
    sub_category = models.ForeignKey('SubCategoryModel', on_delete=models.CASCADE, related_name='products', null=True, blank=False)
    sku_code = models.CharField(max_length=255, verbose_name='SKU Code', null=False, blank=False)
    product_summary = models.TextField(verbose_name='AI Summary Description', null=False, blank=False)
    currency = models.CharField(max_length=255, verbose_name='Currency', null=False, blank=False, default='KES')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=False, blank=False)
        
    class Meta:
        verbose_name = 'Detail Model'
        verbose_name_plural = 'Detail Models'

    def __str__(self):
        return self.name + '-' + self.sku_code
    


'''CATEGORY MODEL'''
class CategoryModel(models.Model):
    category = models.CharField(max_length=255, verbose_name='Category', null=False, blank=False)    
    
    class Meta:
        verbose_name = 'Category Model'
        verbose_name_plural = 'Category Models'

    def __str__(self):
        return self.category
    


'''SUBCATEGORY MODEL'''
class SubCategoryModel(models.Model):
    sub_category = models.CharField(max_length=255, verbose_name='Sub Category', null=False, blank=False)
    
    class Meta:
        verbose_name = 'Sub Category Model'
        verbose_name_plural = 'Sub Category Models'

    def __str__(self):
        return self.sub_category
