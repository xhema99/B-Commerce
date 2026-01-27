📚 B-Commerce - Full Stack Book Marketplace & Messaging System
B-Commerce es una plataforma integral de comercio electrónico para libros que combina un motor de búsqueda avanzado con un sistema de comunicación bidireccional entre usuarios. Los usuarios pueden gestionar sus catálogos, descubrir libros y negociar directamente a través de un chat privado integrado.

🚀 Módulos Destacados
💬 Sistema de Comunicación (Inbox)
Este módulo permite la interacción directa entre la comunidad:

Chats por Producto: Cada conversación está vinculada a un libro específico, facilitando el contexto de la negociación.

Bandeja de Entrada Dinámica: Listado de chats activos que muestra al interlocutor, la imagen del libro y la última fecha de modificación.

Interfaz de Chat: Sistema de mensajes estilizados donde los mensajes propios se diferencian visualmente de los recibidos mediante colores (Blue vs Gray).

Lógica de Seguridad: Validación para evitar que un vendedor inicie un chat consigo mismo y protección de hilos mediante @login_required.

📖 Gestión de Libros & Catálogo
Búsqueda Inteligente: Filtrado por categorías y términos de búsqueda mediante consultas complejas con el objeto Q.

Panel de Vendedor: Espacio privado para que los usuarios gestionen sus publicaciones, editen precios o marquen artículos como vendidos.

🔐 Seguridad y Estilo
Autenticación: Registro y login de usuarios con validación completa de formularios.

Frontend Moderno: Uso intensivo de Tailwind CSS para crear una experiencia de usuario responsiva, con componentes como modales de mensaje y cuadrículas de productos.

🛠️ Detalles de Implementación Técnica
Modelos: Relaciones Many-to-Many para los miembros de una conversación y ForeignKeys para vincular mensajes a hilos y libros.

Forms: Personalización de widgets de Django para inyectar clases de Tailwind directamente en el HTML.

Arquitectura: Separación modular en apps (core, libro, panel, comunicacion) para mantener un código limpio y escalable.
