# Excel vs. una base de datos real

| Aspecto | Excel | Base de datos (MySQL, PostgreSQL...) |
|---------|-------|--------------------------------------|
| **Volumen** | Pocos miles o cientos de miles de filas (límite de ~1.048.576) | Millones o miles de millones de registros |
| **Usuarios simultáneos** | Pocos; puede haber conflictos al editar a la vez | Cientos o miles a la vez, con control de concurrencia |
| **Integridad** | No impide datos repetidos o inconsistentes | Claves primarias y foráneas, restricciones y tipos de datos estrictos |
| **Relaciones** | Hojas sueltas, enlazadas con fórmulas frágiles | Tablas relacionadas formalmente |
| **Consultas** | Filtros y fórmulas | Lenguaje SQL, potente y reutilizable |
| **Seguridad** | Contraseña de archivo | Usuarios, roles y permisos por tabla |
| **Respaldo y recuperación** | Copias manuales | Respaldos, transacciones y recuperación ante fallos |
| **Uso ideal** | Análisis rápido, cálculos y reportes personales | Sistemas de información y aplicaciones en producción |

**Conclusión:** Excel sirve para analizar y presentar datos. Una base de datos sirve para almacenarlos de forma segura, consistente y compartida por una aplicación.
