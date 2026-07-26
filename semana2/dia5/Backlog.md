# Product Backlog & Sprint 1 Planning

## Product Backlog (Sistema de Monitoreo IoT)

| ID | Historia de Usuario | Prioridad (MoSCoW) | Puntos |
|---|---|---|---|
| **US-01** | Como analista de datos, quiero que se registren las lecturas de temperatura y humedad para tener un historial confiable de las condiciones de la bodega. | Must Have | 2
| **US-02** | Como supervisor, quiero que el sistema detecte anomalías cuando la T > 35°C o H > 80% para prevenir daños. | Must Have | 3 |
| **US-03** | Como operador, quiero recibir alertas en la consola cuando haya una anomalía para actuar de inmediato. | Must Have | 2 |
| **US-04** | Como auditor, quiero que las alertas se guarden en un archivo de texto para mantener un registro histórico. | Must Have | 3 |
| **US-05** | Como administrador, quiero poder inyectar los umbrales de anomalía dinámicamente para no depender de valores fijos en el código. | Must Have | 2 |
| **US-06** | Como operador, quiero consultar la última lectura de un sensor específico para conocer el estado actual. | Should Have | 2 |
| **US-07** | Como supervisor, quiero ver un resumen de los 10 sensores activos para monitorear toda la bodega. | Should Have | 3 |
| **US-08** | Como personal de mantenimiento, quiero que el código maneje los errores de datos corruptos para evitar que el sistema colapse de madrugada. | Could Have | 3
| **US-09** | Como administrador, quiero configurar la frecuencia de lectura (ej. 30 segundos) para optimizar el procesamiento. | Could Have | 2 |
| **US-10** | Como auditor, quiero exportar todo el historial del día en un CSV para análisis en Excel. | Won't Have | 5 |

---

## Criterios Gherkin

**US-01: Registro de Lecturas**
* **Given** que el sensor envía una temperatura de 25.0 y humedad de 60.0
* **When** el sistema recibe y procesa la lectura
* **Then** se crea un objeto válido con esos valores exactos.

**US-02: Detección de Anomalías Base**
* **Given** los umbrales estándar de peligro
* **When** el sistema recibe una lectura de T = 36 y H = 50
* **Then** el sistema identifica la lectura como una anomalía.

**US-03: Alerta en Consola**
* **Given** una lectura clasificada como anómala
* **When** el gestor de alertas procesa el evento
* **Then** se imprime un mensaje de advertencia visible en la terminal de texto.

**US-04: Alerta en Archivo**
* **Given** una lectura clasificada como anómala
* **When** el gestor de alertas procesa el evento
* **Then** se añade una nueva línea con los detalles al archivo de registro histórico.

**US-05: Umbrales Dinámicos**
* **Given** un detector instanciado con T > 30 y H > 70
* **When** se evalúa una lectura de T = 32 y H = 60
* **Then** el sistema utiliza los nuevos umbrales y la marca como anomalía.

**US-06: Consulta Individual**
* **Given** un sensor "TEMP-01" con datos registrados
* **When** el operador solicita el estado de "TEMP-01"
* **Then** el sistema devuelve únicamente la lectura más reciente de ese sensor.

**US-07: Resumen General**
* **Given** 10 sensores con información activa
* **When** el supervisor solicita el reporte general
* **Then** el sistema muestra una lista con el estado actual de los 10 dispositivos.

**US-08: Manejo de Errores**
* **Given** que un sensor envía un texto en lugar de un número
* **When** el sistema intenta procesar el dato
* **Then** se captura la excepción y el programa continúa ejecutándose sin colapsar.

**US-09: Frecuencia de Lectura**
* **Given** una configuración de frecuencia de 60 segundos
* **When** el temporizador interno avanza
* **Then** el sistema solo acepta una nueva lectura cuando transcurre ese intervalo.

**US-10: Exportación CSV**
* **Given** un registro de lecturas de todo el día
* **When** el auditor ejecuta el comando de exportación
* **Then** se genera un archivo separado por comas con todos los datos ordenados por fecha.

