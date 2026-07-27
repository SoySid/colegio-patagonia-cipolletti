from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .admin import CarruselMultipleForm


class CarruselMultipleFormTests(TestCase):
    def test_form_collects_multiple_files(self):
        file1 = SimpleUploadedFile("img1.jpg", b"file1", content_type="image/jpeg")
        file2 = SimpleUploadedFile("img2.jpg", b"file2", content_type="image/jpeg")

        form = CarruselMultipleForm(
            data={"orden": 0, "activa": True},
            files={"imagenes_multiples": [file1, file2]},
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(len(form.cleaned_data["imagenes_multiples"]), 2)
