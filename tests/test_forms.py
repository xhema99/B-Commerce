import pytest
from libro.forms import NuevoLibro, EditarLibro
from core.forms import CrearcuentaForm

pytestmark = pytest.mark.django_db


class TestNuevoLibroForm:
    def test_campos_requeridos(self):
        form = NuevoLibro(data={})
        assert not form.is_valid()
        assert 'nombre' in form.errors
        assert 'precio' in form.errors
        assert 'categoria' in form.errors

    def test_datos_validos(self, categoria):
        form = NuevoLibro(data={
            'categoria': categoria.id,
            'nombre': 'Mi libro',
            'precio': 15.99,
        })
        assert form.is_valid()

    def test_precio_invalido(self, categoria):
        form = NuevoLibro(data={
            'categoria': categoria.id,
            'nombre': 'Mi libro',
            'precio': -5,
        })
        assert not form.is_valid()


class TestCrearcuentaForm:
    def test_campos_requeridos(self):
        form = CrearcuentaForm(data={})
        assert not form.is_valid()

    def test_password_no_coinciden(self):
        form = CrearcuentaForm(data={
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'complex123',
            'password2': 'different',
        })
        assert not form.is_valid()
