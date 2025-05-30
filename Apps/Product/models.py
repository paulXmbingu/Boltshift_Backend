from django.db import models






class DetailModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=False, blank=False)
    sku_code = models.CharField(max_length=255, verbose_name='SKU Code', null=False, blank=False)
    product_summary = models.TextField(verbose_name='AI Summary Description', null=False, blank=False)
    currency = models.CharField(max_length=255, verbose_name='Currency', null=False, blank=False, default='KES')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=False, blank=False)
        
    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'

    def __str__(self):
        return self.name + '-' + self.sku_code





class BrandModel(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Brand', null=False, blank=False)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand





class CategoryModel(models.Model):
    category = models.CharField(max_length=255, verbose_name='Category', null=False, blank=False)    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category
    




class SubCategoryModel(models.Model):
    sub_category = models.CharField(max_length=255, verbose_name='Sub Category', null=False, blank=False)
    
    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.sub_category





class PhotosModel(models.Model):
    product_photos = models.ImageField(upload_to='Product_Photos/', null=False, blank=False)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.product_photos.name





class VideosModel(models.Model):
    product_videos = models.FileField(upload_to='Product_Videos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.product_videos.name





class ShowRatingModel(models.Model):
    average_star_ratings = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Average Star Ratings', null=True, blank=True)
    five_star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='5 Star Rating', null=True, blank=True)
    four_star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='4 Star Rating', null=True, blank=True)
    three_star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='3 Star Rating', null=True, blank=True)
    two_star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='2 Star Rating', null=True, blank=True)
    one_star_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='1 Star Rating', null=True, blank=True)

    class Meta:
        verbose_name = 'Star Rating'
        verbose_name_plural = 'Star Ratings'
    
    def __str__(self):
        return f'Star Rating'





class ReviewModel(models.Model):
    reviews_count = models.IntegerField(verbose_name='Review Count', null=True, blank=True)

    class Meta:
        verbose_name = 'Review Count'
        verbose_name_plural = 'Reviews Count'

    def __str__(self):
        return str(self.reviews_count)





class InventoryMeterModel(models.Model):
    remaining_items = models.IntegerField(verbose_name='Remaining Items', null=False, blank=False)
    total_items = models.IntegerField(verbose_name='Total Items', null=False, blank=False)

    class Meta:
        verbose_name = 'Inventory Meter'
        verbose_name_plural = 'Inventory Meters'

    def __str__(self):
        return f'{self.remaining_items} out of  {self.total_items}'





class Option1Model(models.Model):
    option_1_selector = models.CharField(max_length=255, verbose_name='Option 1 Selector', null=False, blank=False)

    class Meta:
        verbose_name = 'Option 1'
        verbose_name_plural = 'Options 1'
    
    def __str__(self):
        return f'Opt 1 {self.option_1_selector}'
    




class Option2Model(models.Model):
    option_2_selector = models.CharField(max_length=255, verbose_name='Option 2 Selector', null=False, blank=False)

    class Meta:
        verbose_name = 'Option 2'
        verbose_name_plural = 'Options 2'
    
    def __str__(self):
        return f'Opt 2 {self.option_2_selector}'
    




class TagsModel(models.Model):
    tag_list = models.CharField(max_length=255, verbose_name='Tags List', null=False, blank=False)

    class Meta:
        verbose_name = 'Tags List'
        verbose_name_plural = 'Tags Lists'
    
    def __str__(self):
        return self.tag_list
    




class DescriptionModel(models.Model):
    long_description = models.TextField(verbose_name='Long Description', null=False, blank=False)

    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'
    
    def __str__(self):
        return self.long_description
    




class SpecificationModel(models.Model):
    specification = models.TextField(verbose_name='Specification', null=False, blank=False)

    class Meta:
        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'
    
    def __str__(self):
        return self.specification

