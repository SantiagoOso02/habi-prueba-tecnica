# Prueba técnica para el puesto de desarrollador backend en Habi

Esta prueba consiste en desarrollar un microservicio REST para consultar información de inmuebles almacenados en una base de datos MySQL. El desarrollo se realiza completamente en Python nativo, sin frameworks ni ORMs, siguiendo la metodología TDD (Test-Driven Development).

## Tecnologías utilizadas y enfoque del desarrollo

### Tecnologías utilizadas

- Python 3.9+

- MySQL (conexión directa mediante mysql-connector-python)

- unittest (para pruebas unitarias)
  
- dotenv (para manejo de configuración de las variables de entorno)
  
- PEP8 como guía de estilo
  
 - Sin uso de frameworks web o ORMs

### Enfoque de desarrollo 

Este proyecto se desarrollará siguiendo TDD (Test-Driven Development). Esto significa que:

1. Se escribirá primero una prueba unitaria que refleje el comportamiento deseado.

2. Luego se desarrollará el código mínimo necesario para que la prueba pase.

3. Finalmente se refactorizará el código manteniendo las pruebas verdes.

### Estructura del proyecto
```
habi-prueba-tecnica/
├── src/
│   ├── api/               # Servidor REST para el API del MS
│   ├── database/          # Conexión a la base de datos
│   ├── models/            # Clases que representan entidades del dominio
│   ├── services/          # Lógica de negocio
├── tests/                 # Pruebas unitarias
├── docs/                  # Documentación y archivos SQL correpondientes al microservicio de "Me gusta"
└── .env
└── .gitignore
└── README.md
└── requirements.txt
```

# Servicio de "consulta"

Este microservicio expone un endpoint REST que permite consultar inmuebles disponibles en la base de datos. Los datos se obtienen directamente de una base MySQL mediante SQL nativo (sin ORM) y se filtran según el último estado registrado del inmueble.

## Funcionalidades implementadas

- Consulta de propiedades cuyo último estado sea `pre_venta`, `en_venta` o `vendido`
- Filtro opcional por:
  - Año de construcción (`year`)
  - Ciudad (`city`)
  - Estado actual (`status`)
- Combinación de múltiples filtros en una misma consulta
- Validaciones de entrada para cada filtro
- Respuestas consistentes en formato JSON
- Manejo de errores con códigos HTTP apropiados
- Endpoint `/health` para verificación de salud del servicio

## Endpoint REST

### `GET /properties`

Devuelve una lista de propiedades visibles, opcionalmente filtradas.

**Parámetros de query:**
| Parámetro | Tipo     | Descripción                                       |
|-----------|----------|---------------------------------------------------|
| `year`    | int      | Año de construcción de la propiedad               |
| `city`    | string   | Ciudad exacta (ejemplo: `Bogotá`)                |
| `status`  | string   | Uno de: `pre_venta`, `en_venta`, `vendido`       |

Cabe aclarar que a pesar de que en `docs/filters.json` está los posibles filtros, este archivo es de mera información y no tiene ningún propósito de prueba, todos los filtros son tratados a través de parámetros.


#### **Ejemplos de uso:**


`/properties`


`/properties?city=Bogotá`


`/properties?year=2020&status=pre_venta`


`/properties?status=en_venta&year=2020&city=pereira`



Errores posibles:

| Error| Motivo | 
|----------|----------|
| 400    | Filtro inválido o valor no permitido   |
| 404    | Endpoint no encontrado   |
| 500    | Error interno del servidor   |

### Pruebas 
El microservicio fue desarrollado completamente con TDD. Las pruebas unitarias cubren:

- Filtros individuales (year, city, status)

- Filtros combinados

- Validación del contenido y estructura de las propiedades

- Las pruebas están ubicadas en la carpeta `tests/`.

### Colecciones de Postman
Se incluye una colección de Postman en `collections/` para facilitar el consumo y prueba del microservicio. Puede ser importada directamente desde la aplicación Postman.

# Servicio de "Me gusta"
