from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Product'
    verbose_name = 'Product Management'
    label = 'product_app'
    