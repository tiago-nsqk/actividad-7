SOLUCION ACTIVIDAD 7 , EXCEL , EXPLICACION DE BOLEANOS ETC PARTE 1 DE LA ACTIVIDAD. Punto 1: Bases de datos, tipos de datos y reflexiones

1 y 2. Tipos de datos más comunes (máximo 3 ejemplos de cada uno)

Tipo	¿Qué guarda?	Ejemplos en situaciones reales
INT	Números enteros (sin decimales)	1) Edad de un paciente ( 23). 2) Cantidad en stock de un producto ( 150). 3) Número de documento de identidad ( 1012345678, aunque si hay ceros a la izquierda es mejor VARCHAR).
VARCHAR(n)	Texto de longitud variable, hasta n caracteres	1) Nombre de un cliente ( 'Laura Torres'). 2) Correo electrónico ( 'laura@correo.com'). 3) Placa de un vehículo ( 'ABC123').
FECHA	Una fecha (AAAA-MM-DD)	1) Fecha de nacimiento ( '2003-05-14'). 2) Fecha de una cita médica. 3) Fecha de una venta o factura.
DECIMAL(p,s)	Números exactos con decimales (ideal para dinero)	1) Precio de un producto ( DECIMAL(10,2)→ 1999.90). 2) Saldo de una cuenta bancaria. 3) Peso de un paquete ( 2.35kg).
BOOLEO	Verdadero / falso	1) Si un producto está activo. 2) Si una factura fue pagada. 3) Si un usuario aceptó los términos.
TEXTO	Texto largo	1) Descripción de un producto. 2) Observaciones de una historia clínica. 3) Comentarios de un cliente.
FECHA Y HORA / MARCA DE TIEMPO	Fecha y hora	1) Momento exacto de una transacción. 2) Hora de ingreso a una plataforma. 3) Fecha y hora de creación de un registro.
Por qué importa elegir bien el tipo:** ocupa menos espacio, valida los datos (no se puede guardar "hola" en un INT) y permite operar (sumar precios, ordenar fechas, calcular edades). Para dinero se usa DECIMAL y no FLOAT, porque FLOAT puede generar errores de redondeo.

¿Qué pienso cuando escucho "No hay sistema"?
Pienso en una persona esperando en una fila, mientras el empleado dice que no puede hacer nada porque el ordenador "se cayó". La frase muestra que hoy casi todo el proceso depende de un sistema informático. Si falla o no existe:

Pérdida de datos: si la información estaba en papel o en un solo equipo, un incendio, un daño o un descubierto la borra para siempre.
Ineficiencia: buscar un expediente en un archivador toma minutos u horas, no segundos.
Errores: con cálculos y transcripciones manuales aparecen duplicados, cobros incorrectos y datos mal escritos.
Falta de trazabilidad y seguridad: no se sabe quién cambió qué, y cualquiera con acceso al papel puede alterarlo.
Impacto en las personas: pagos que no se registran, citas médicas que se pierden, pedidos que no llegan y clientes molestos o perjudicados.
Impacto en banca, salud y comercio, y 3 ejemplos históricos
Banca: sin sistemas no hay cajeros, transferencias ni verificación de saldos en tiempo real. Todo dependería de libros contables y sucursales.
Salud: sin historia clínica electrónica se pierden alergias, diagnósticos y exámenes, lo que puede causar errores médicos.
Comercio: sin inventario ni punto de venta se vende lo que no hay, o se deja de vender lo que sí hay.
Ejemplos históricos donde fallaron o faltaron los sistemas:

Fallo de los sistemas de TSB Bank (Reino Unido, 2018): una migración informática fallida dejó a millones de clientes sin acceso a sus cuentas, y algunos vieron datos de otras personas.
Apagón de CrowdStrike / Windows (julio 2024): una actualización defectuosa dejó millones de equipos inutilizables. Se cancelaron millas de vuelos y hubo problemas en hospitales y bancos.
Ciberataque de WannaCry al NHS (Reino Unido, 2017): hospitales perdieron acceso a sus sistemas y tuvieron que cancelar citas y operaciones y volver al papel.
Antes de las computadoras
Las transacciones bancarias se hacían en la sucursal: se llenaban formularios en papel, un cajero anotaba en libros contables y se verificaba la firma contra una tarjeta física. Las solicitudes médicas se hacían yendo en persona a pedir cita, y las historias clínicas eran carpetas de papel guardadas en archivadores.

Cuadro comparativo: antes vs. ahora
Proceso	Antes de la tecnología	Ahora con sistemas informáticos
Consignar o transferir dinero	Ir a la sucursal, hacer fila y llenar un formulario	App móvil o banca en línea, en segundos y 24/7
Consultar saldo	Pedir un extracto impreso o preguntar al cajero	Consulta inmediata desde el celular.
Pedir cita médica	Ir o llamar por teléfono, con agenda en papel	Portal o app con agenda en línea y recordatorios
Historia clínica	Carpeta física en un archivador, difícil de compartir	Historia electrónica accesible desde cualquier sede autorizada.
Inventario de una tienda	Conteo manual y cuaderno	Sistema que desconta el stock en cada venta
Comprar	Solo en tienda, pagando en efectivo	Comercio electrónico con pagos digitales
Búsqueda de información	Revisar archivadores a mano	Consulta SQL o buscador en segundos
Copias de seguridad	Fotocopias	Respaldos automáticos en la nube
Errores	Frecuentes (manual de transcripción)	Menos errores gracias a validaciones
:		
PUNTO 7,8,9,10,11 DESARROLLA LAS TABLAS EN EXCEL TENIENDO EN CUENTA LOS GUSTOS DE TUS COMPAÑEROS:		
REALIZA 3 TABLAS DINAMICAS Y AL FINAL UN ESTILO BASE DE DATOS PARA PODER HACER LA COMPARACION CON UNA MEJOR:		
1:imagen		
2:imagen		
3:imagen		
4:imagen		
esta fue la parte de Excel que hice gracias a unos compañeros de mi clase, no se hicieron tablas muy grandes por que el tiempo no alcanzo pero		
me gustó la dinámica.		
Excel vs. una base de datos reales
Aspecto	Sobresalir	Base de datos (MySQL, PostgreSQL...)
Volumen	Pocos millas o cientos de millas de filas (límite de ~1.048.576)	Millones o millas de millones de registros
Usuarios simultáneos	Pocos; puede haber conflictos al editar a la vez	Cientos o millas a la vez, con control de concurrencia
Integridad	No impide datos repetidos o inconsistentes	Claves primarias y foráneas, restricciones y tipos de datos estrictos
Relaciones	Hojas sueltas, enlazadas con fórmulas frágiles	Tablas relacionadas formalmente
Consultas	Filtros y fórmulas	Lenguaje SQL, potente y reutilizable
Seguridad	Contraseña de archivo	Usuarios, roles y permisos por tabla
Respaldo y recuperación	Copias manuales	Respaldos, transacciones y recuperación ante fallos
Uso ideal	Análisis rápido, cálculos e informes personales.	Sistemas de información y aplicaciones en producción.
Conclusión: Excel sirve para analizar y presentar datos. Una base de datos sirve para almacenarlos de forma segura, consistente y compartida por una aplicación.

PARTE 2, LIBRERIAS Y FILOSOFIAS DE PYTHON Y SQL:

El Zen de Python: Consiste en 19 aforismos accesibles mediante import thisen la consola de Python (PEP 20), cuyo propósito principal es promover la escritura de código limpio, simple y legible. El principio destacado es "Readability counts" (la legibilidad cuenta), fundamental tanto en programación como en el diseño de bases de datos para facilitar su mantenimiento por parte de múltiples personas.
Desarrollo con Python y MySQL: El proceso abarca la conexión mediante mysql-connector-python, la creación de la base de datos ( actividad7) y sus respectivas tablas ( automovil, paciente, producto), la inserción de registros, la ejecución de consultas de filtrado, modificación y eliminación, y la integración de los resultados en un DataFrame de pandas.
Librerías de análisis y su integración con MySQL:
pandas: Enfocada en la manipulación de datos tabulares, destacando por su amplia adopción y documentación.
polars: Alternativa optimizada orientada al rendimiento en velocidad y uso eficiente de memoria mediante evaluación perezosa y procesamiento multinúcleo.
scipy: Diseñada para cálculos científicos, estadísticos y matemáticos avanzados sobre conjuntos numéricos.
Integración: Se detalla cómo conectar Python con MySQL tanto en entornos remotos y temporales ( Google Colab ) como en entornos locales persistentes ( Visual Studio Code ), recomendando el uso de prácticas seguras para la gestión de credenciales (Secretos y archivos .env).
imagen
PARTE 3 MISQL DESDE PYTHON,. ESTA EN EL ARCHIVO SUBIDO DESDE UN ARCHIVO AL REPIOSITORIO. 📊 Infografía: Integración de MySQL con Python (Alcance y Aplicaciones)1. Conexión y Herramientas Principales Para vincular el poder dinámico de Python con la robustez relacional de MySQL, se emplean librerías y conectores especializados: mysql-connector-python: El conector oficial desarrollado por Oracle, escrito puramente en Python, ideal para una integración directa y sencilla mediante pip. PyMySQL: Una alternativa ligera escrita 100% en Python, muy compatible y fácil de configurar. SQLAlchemy / Peewee (ORMs): Permite mapear tablas relacionales como objetos de Python, evitando escribir consultas manuales SQL y acelerando el desarrollo de software moderno.2. Flujo de Trabajo TípicoEl proceso estándar para gestionar datos entre ambos entornos sigue una estructura ciclodo:PasoAcción en PythonDescripción Técnica1. Conexiónmysql.connector.connect(...)Establece el canal seguro de comunicación usando credenciales y sockets/SSL.2. Cursordb.cursor()Crea un objeto iterador para enviar comandos SQL y recuperar filas de resultados.3. Ejecucióncursor.execute(query)Envía sentencias operativas (SELECT, INSERT, UPDATE, DELETE).4. Cierrecursor.close() / db.close()Libera los recursos del servidor de bases de datos de forma limpia.3. Aplicaciones Actuales en el MercadoLa combinación de Python y MySQL impulsa soluciones tecnológicas avanzadas en diversos sectores:Desarrollo Web y APIs: Soporte de bases de datos relacionales para backends robustos construidos con frameworks como Django o Flask y FastAPI.Paneles de Control (Dashboards) y BI: Extracción masiva de datos mediante Python (pandas, matplotlib) para alimentar informes gerenciales almacenados en MySQL.Automatización e IoT: Ingesta continua de métricas generadas por dispositivos conectados directamente hacia tablas relacionales estructuradas.Inteligencia Artificial y GenAI: Con el soporte moderno para módulos orientados a machine learning, permite almacenar metadatos de modelos, registros conversacionales y consultas optimizadas para pipelines analíticos.4. Alcance y Ventajas Clave¿Por qué elegir esta dupla?Escalabilidad: Capacidad para manejar millones de registros con índices optimizados.Ecosistema: Acceso a la inmensa cantidad de librerías de análisis de datos de Python combinados con la seguridad transaccional ACID de MySQL.Tutorial paso a paso para conectar Python con MySQLEste video resulta útil para observar de manera práctica el proceso de configuración inicial y la ejecución de consultas básicas entre ambos entornos.

Me base en este video para la vinculación de MySQL a python: https://youtu.be/TjaNXqatHYs?si=HOlscsM9pqAi9RrG

la actividad estuvo bastante interesante , logre entender las tantas aplicaciones y librerías que tiene Python, aprendí de cultura gracias ha hallazgos y proyectos innovadores de varios autores, y ya aprendí a manejare mejor los terminales DE VISUAL ESTUDIO CODE GRACIAS;)
