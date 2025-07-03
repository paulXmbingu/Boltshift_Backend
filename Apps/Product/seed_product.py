import os
import sys
import django
import random
from decimal import Decimal
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
from faker import Faker

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Set the correct settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
django.setup()

from Apps.Product.models import (
    DetailModel, SummaryDescriptionModel, BrandModel, CategoryModel,
    SubCategoryModel, PhotosModel, VideosModel, ShowRatingModel,
    ReviewModel, InventoryMeterModel, Option1Model, Option2Model,
    TagsModel, DescriptionModel, SpecificationModel
)

fake = Faker()

def create_fake_image_file(name="image.jpg"):
    img = Image.new("RGB", (100, 100), color=(random.randint(0, 255), 0, 0))
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return ContentFile(buffer.getvalue(), name=name)

def run():
    for _ in range(20):
        DetailModel.objects.create(
            name=fake.word(),
            sku_code=fake.unique.bothify('SKU-####'),
            currency='KES',
            price=Decimal(fake.pydecimal(left_digits=4, right_digits=2, positive=True))
        )

        SummaryDescriptionModel.objects.create(summary_description=fake.sentence())

        BrandModel.objects.create(brand=fake.company())

        CategoryModel.objects.create(category=fake.word())

        SubCategoryModel.objects.create(sub_category=fake.word())

        PhotosModel.objects.create(
            product_photos=create_fake_image_file(fake.unique.word() + ".jpg")
        )

        VideosModel.objects.create(
            product_videos=ContentFile(b"fake video data", name=fake.unique.word() + ".mp4")
        )

        ShowRatingModel.objects.create(
            average_star_ratings=round(random.uniform(1.0, 5.0), 1),
            five_star_rating=round(random.uniform(0.0, 5.0), 1),
            four_star_rating=round(random.uniform(0.0, 5.0), 1),
            three_star_rating=round(random.uniform(0.0, 5.0), 1),
            two_star_rating=round(random.uniform(0.0, 5.0), 1),
            one_star_rating=round(random.uniform(0.0, 5.0), 1),
        )

        ReviewModel.objects.create(reviews_count=random.randint(0, 300))

        InventoryMeterModel.objects.create(
            remaining_items=random.randint(0, 100),
            total_items=100
        )

        Option1Model.objects.create(option_1_selector=fake.word())

        Option2Model.objects.create(option_2_selector=fake.word())

        TagsModel.objects.create(tag_list=', '.join(fake.words(3)))

        DescriptionModel.objects.create(long_description=fake.paragraph())

        SpecificationModel.objects.create(specification=fake.text(max_nb_chars=150))

if __name__ == "__main__":
    run()
