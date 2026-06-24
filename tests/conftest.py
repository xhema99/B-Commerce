import os
import sys

import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, BASE_DIR)


@pytest.fixture
def categoria(db):
    from libro.models import Categoria
    return Categoria.objects.create(name='Novela')


@pytest.fixture
def usuario(db):
    from django.contrib.auth.models import User
    return User.objects.create_user(
        username='testuser',
        password='testpass123',
        email='test@example.com'
    )


@pytest.fixture
def usuario2(db):
    from django.contrib.auth.models import User
    return User.objects.create_user(
        username='testuser2',
        password='testpass123',
        email='test2@example.com'
    )


@pytest.fixture
def libro(db, categoria, usuario):
    from libro.models import Libro
    return Libro.objects.create(
        categoria=categoria,
        nombre='Libro de prueba',
        descripcion='Descripcion de prueba',
        precio=19.99,
        creado_por=usuario,
    )


@pytest.fixture
def client():
    from django.test import Client
    return Client()
