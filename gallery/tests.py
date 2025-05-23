from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Image
from datetime import date

class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category(name="Nature")
        self.assertEqual(str(category), "Nature")

    def test_create_category(self):
        category = Category.objects.create(name="Travel")
        self.assertEqual(category.name, "Travel")


class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Art")
        self.category2 = Category.objects.create(name="Photography")

    def test_create_image(self):
        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61',  # simple fake GIF content
            content_type='image/gif'
        )
        image = Image.objects.create(
            title="Sunset",
            image=image_file,
            age_limit=12
        )
        image.categories.set([self.category1, self.category2])
        image.save()

        self.assertEqual(image.title, "Sunset")
        self.assertEqual(image.age_limit, 12)
        self.assertIn(self.category1, image.categories.all())
        self.assertIn(self.category2, image.categories.all())
        self.assertIsInstance(image.created_date, date)
        self.assertEqual(str(image), "Sunset")
