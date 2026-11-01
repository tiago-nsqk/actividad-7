# Tipos de datos más comunes (máximo 3 ejemplos de cada uno)

| Tipo | ¿Qué guarda? | Ejemplos en situaciones reales |
|------|--------------|--------------------------------|
| **INT** | Números enteros (sin decimales) | 1) Edad de un paciente (`23`). 2) Cantidad en stock de un producto (`150`). 3) Número de documento de identidad (`1012345678`, aunque si hay ceros a la izquierda es mejor VARCHAR). |
| **VARCHAR(n)** | Texto de longitud variable, hasta n caracteres | 1) Nombre de un cliente (`'Laura Torres'`). 2) Correo electrónico (`'laura@correo.com'`). 3) Placa de un vehículo (`'ABC123'`). |
| **DATE** | Una fecha (AAAA-MM-DD) | 1) Fecha de nacimiento (`'2003-05-14'`). 2) Fecha de una cita médica. 3) Fecha de una venta o factura. |
| **DECIMAL(p,s)** | Números exactos con decimales (ideal para dinero) | 1) Precio de un producto (`DECIMAL(10,2)` → `1999.90`). 2) Saldo de una cuenta bancaria. 3) Peso de un paquete (`2.35` kg). |
| **BOOLEAN** | Verdadero / falso | 1) Si un producto está activo. 2) Si una factura fue pagada. 3) Si un usuario aceptó los términos. |
| **TEXT** | Texto largo | 1) Descripción de un producto. 2) Observaciones de una historia clínica. 3) Comentarios de un cliente. |
| **DATETIME / TIMESTAMP** | Fecha y hora | 1) Momento exacto de una transacción. 2) Hora de ingreso a una plataforma. 3) Fecha y hora de creación de un registro. |

**Por qué importa elegir bien el tipo:** ocupa menos espacio, valida los datos (no se puede guardar "hola" en un INT) y permite operar (sumar precios, ordenar fechas, calcular edades). Para dinero se usa DECIMAL y no FLOAT, porque FLOAT puede generar errores de redondeo.
