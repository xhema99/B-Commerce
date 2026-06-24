import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestFlujoCompleto:
    def test_registro_login_publicacion(self, client, categoria):
        response = client.post(reverse('core:crearcuenta'), {
            'username': 'lector',
            'email': 'lector@example.com',
            'password1': 'pass1234complex',
            'password2': 'pass1234complex',
        })
        assert response.status_code == 302

        response = client.post(reverse('core:login'), {
            'username': 'lector',
            'password': 'pass1234complex',
        })
        assert response.status_code == 302

        response = client.post(reverse('libro:nuevo'), {
            'categoria': categoria.id,
            'nombre': 'Mi libro publicado',
            'precio': 15.50,
        })
        assert response.status_code == 302

        response = client.get(reverse('panel:index'))
        assert response.status_code == 200
        assert 'Mi libro publicado' in response.content.decode()
