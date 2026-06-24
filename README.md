
# 📚 B-Commerce

**Marketplace de compraventa de libros usados entre particulares.**

Un marketplace moderno donde los amantes de la lectura pueden comprar y vender libros de segunda mano. Construido con Django y Tailwind CSS, con un enfoque en experiencia de usuario, rendimiento y buenas prácticas de desarrollo.

---

## ✨ Características

- **Catálogo completo** con búsqueda avanzada, filtros por categoría y ordenación
- **Sistema de autenticación** con registro, inicio de sesión y perfiles de usuario
- **Panel de usuario** para gestionar publicaciones
- **Mensajería integrada** entre compradores y vendedores
- **Diseño responsive y premium** con sistema de diseño propio
- **Soft delete** en lugar de eliminación física de registros
- **Manejo seguro de precios** con `DecimalField` y validación
- **Preparado para producción** con Docker, GitHub Actions y configuración por entornos

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| **Backend** | Django 5.0.7 + Python 3.12 |
| **Base de datos** | SQLite (desarrollo) / PostgreSQL 16 (producción) |
| **Frontend** | Tailwind CSS 3 + Django Templates (SSR) |
| **Testing** | pytest + pytest-django (28 tests) |
| **Infraestructura** | Docker, docker-compose, GitHub Actions |
| **Calidad** | Ruff, Black, isort |

---

## 🚀 Inicio rápido

```bash
# Clonar e instalar
git clone https://github.com/xhema99/B-Commerce.git
cd B-Commerce

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements-dev.txt
cp .env.example .env

# Compilar assets
npm install
npm run build:css

# Base de datos y servidor
python manage.py migrate
python manage.py runserver
```

Abrir [http://localhost:8000](http://localhost:8000) 🎉

---

## 🐳 Docker (producción)

```bash
docker compose up --build
```

---

## 📁 Estructura del proyecto

```
.
├── apps/
│   ├── core/              # Landing, autenticación
│   ├── libro/             # Catálogo y CRUD de libros
│   ├── panel/             # Panel del usuario
│   └── comunicacion/      # Mensajería entre usuarios
├── config/
│   └── settings/          # Configuración por entorno
│       ├── base.py
│       ├── local.py
│       ├── production.py
│       └── test.py
├── static/                # Assets (CSS, JS)
├── templates/             # Templates base y componentes
├── tests/                 # Tests (28 tests)
├── .github/workflows/     # CI/CD
└── Dockerfile / docker-compose.yml
```

---

## 🔧 Comandos útiles

```bash
make run          # Iniciar servidor de desarrollo
make test         # Ejecutar tests
make check        # Validar proyecto
make css          # Compilar Tailwind CSS
make migrate      # Ejecutar migraciones
```

---

## 📊 Testing

```bash
pytest tests/ --ds=config.settings.test -v --cov
```

Actualmente **28 tests** pasando, cubriendo modelos, formularios, vistas, permisos y flujos completos.

---

## 🏗️ Arquitectura

- **Server-Side Rendering** con Django Templates
- **4 apps modulares** con responsabilidades bien delimitadas
- **Settings separados** por entorno (desarrollo, producción, testing)
- **ORM optimizado** con `select_related` y `prefetch_related`
- **Señales** para eventos como nuevos mensajes
- **Sistema de diseño propio** con Tailwind CSS y paleta personalizada

---

## 🎨 Paleta de colores

| Color | Código |
|-------|--------|
| Primary | `#92B1A5` |
| Primary Dark | `#7A9C90` |
| Secondary | `#DA8C91` |
| Accent | `#DEB4C4` |
| Neutral | `#DDD2D2` |
| Background | `#F8F6F4` |
| Text | `#2E2E2E` |

---

## 📄 Licencia

MIT
