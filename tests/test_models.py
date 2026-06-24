import pytest
from django.db import models

from libro.models import Categoria, Libro

pytestmark = pytest.mark.django_db


class TestCategoriaModel:
    def test_campos(self):
        campo = Categoria._meta.get_field('name')
        assert isinstance(campo, models.CharField)
        assert campo.max_length == 200

    def test_str(self, categoria):
        assert str(categoria) == 'Novela'

    def test_ordering(self):
        assert Categoria._meta.ordering == ('name',)


class TestLibroModel:
    def test_campos_requeridos(self):
        assert Libro._meta.get_field('nombre')
        assert isinstance(Libro._meta.get_field('precio'), models.DecimalField)
        assert Libro._meta.get_field('precio').max_digits == 10
        assert Libro._meta.get_field('precio').decimal_places == 2

    def test_soft_delete_fields(self, libro):
        assert libro.activo is True
        assert libro.eliminado_en is None

    def test_str(self, libro):
        assert str(libro) == 'Libro de prueba'

    def test_creacion_completa(self, categoria, usuario):
        libro = Libro.objects.create(
            categoria=categoria,
            nombre='Otro libro',
            descripcion='Desc',
            precio=9.99,
            creado_por=usuario,
        )
        assert libro.pk is not None
        assert libro.vendido is False
        assert libro.activo is True
