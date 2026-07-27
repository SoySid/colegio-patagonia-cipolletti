from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .admin import CarruselMultipleForm, DatosEscuelaAdmin
from .models import DatosEscuela


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


class DatosEscuelaAdminTests(TestCase):
    def test_admin_exposes_logo_field(self):
        admin_instance = DatosEscuelaAdmin(DatosEscuela, admin.site)
        form_class = admin_instance.get_form(None)

        self.assertIn("logo", form_class.base_fields)

    def test_admin_exposes_hero_fields(self):
        admin_instance = DatosEscuelaAdmin(DatosEscuela, admin.site)
        form_class = admin_instance.get_form(None)

        self.assertIn("hero_tag", form_class.base_fields)
        self.assertIn("hero_titulo", form_class.base_fields)
        self.assertIn("hero_subtitulo", form_class.base_fields)
        self.assertIn("hero_imagen", form_class.base_fields)
