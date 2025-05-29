from django.db import models



class DetailModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=False, blank=False)
    brand = models.CharField(max_length=255, verbose_name='Brand', null=False, blank=False)
    sku_code = models.CharField(max_length=255, verbose_name='SKU Code', null=False, blank=False)
    product_summary = models.TextField(verbose_name='AI Summary Description', null=False, blank=False)
    currency = models.CharField(max_length=255, verbose_name='Currency', null=False, blank=False, default='KES')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=False, blank=False)
        
    class Meta:
        verbose_name = 'Detail Model'
        verbose_name_plural = 'Detail Models'

    def __str__(self):
        return self.name + '-' + self.sku_code
    


class CategoryModel(models.Model):
    category = models.CharField(max_length=255, verbose_name='Category', null=False, blank=False)    
    
    class Meta:
        verbose_name = 'Category Model'
        verbose_name_plural = 'Category Models'

    def __str__(self):
        return self.category
    


class SubCategoryModel(models.Model):
    sub_category = models.CharField(max_length=255, verbose_name='Sub Category', null=False, blank=False)
    
    class Meta:
        verbose_name = 'Sub Category Model'
        verbose_name_plural = 'Sub Category Models'

    def __str__(self):
        return self.sub_category



class PhotosModel(models.Model):
    product_photos = models.ImageField(upload_to='Product_Photos/')

    class Meta:
        verbose_name = 'Photos Model'
        verbose_name_plural = 'Photos Models'

    def __str__(self):
        return self.product_photos.name
    

    

class VideosModel(models.Model):
    product_videos = models.FileField(upload_to='Product_Videos/')

    class Meta:
        verbose_name = 'Video Model'
        verbose_name_plural = 'Video Models'

    def __str__(self):
        return self.product_videos.name


