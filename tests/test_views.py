import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestLandingPage:
    def test_status_code(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_template(self, client):
        response = client.get('/')
        assert 'core/index.html' in [t.name for t in response.templates]


class TestRegistro:
    def test_formulario_carga(self, client):
        response = client.get(reverse('core:crearcuenta'))
        assert response.status_code == 200

    def test_registro_exitoso(self, client):
        response = client.post(reverse('core:crearcuenta'), {
            'username': 'nuevousuario',
            'email': 'nuevo@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        assert response.status_code == 302

    def test_registro_fallido(self, client):
        response = client.post(reverse('core:crearcuenta'), {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        })
        assert response.status_code == 200


class TestLogin:
    def test_login_exitoso(self, client, usuario):
        response = client.post(reverse('core:login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        assert response.status_code == 302

    def test_login_fallido(self, client):
        response = client.post(reverse('core:login'), {
            'username': 'noexiste',
            'password': 'nada',
        })
        assert response.status_code == 200


class TestCatalogo:
    def test_listado(self, client, libro):
        response = client.get(reverse('libro:libros'))
        assert response.status_code == 200
        assert libro.nombre in response.content.decode()

    def test_busqueda(self, client, libro):
        response = client.get(reverse('libro:libros'), {'consulta': 'prueba'})
        assert response.status_code == 200

    def test_detalle(self, client, libro):
        response = client.get(reverse('libro:detalles', args=[libro.pk]))
        assert response.status_code == 200
        assert libro.nombre in response.content.decode()


class TestCRUDLibro:
    def test_crear_requiere_login(self, client):
        response = client.get(reverse('libro:nuevo'))
        assert response.status_code == 302

    def test_crear_libro(self, client, usuario, categoria):
        client.force_login(usuario)
        response = client.post(reverse('libro:nuevo'), {
            'categoria': categoria.id,
            'nombre': 'Libro nuevo',
            'precio': 25.00,
        })
        assert response.status_code == 302

    def test_editar_propio(self, client, usuario, libro):
        client.force_login(usuario)
        response = client.post(reverse('libro:editar', args=[libro.pk]), {
            'nombre': 'Editado',
            'precio': 30.00,
        })
        assert response.status_code == 302

    def test_editar_requiere_dueno(self, client, usuario2, libro):
        client.force_login(usuario2)
        response = client.get(reverse('libro:editar', args=[libro.pk]))
        assert response.status_code == 404

    def test_soft_delete(self, client, usuario, libro):
        client.force_login(usuario)
        response = client.post(reverse('libro:eliminar', args=[libro.pk]))
        assert response.status_code == 302
        libro.refresh_from_db()
        assert libro.activo is False
