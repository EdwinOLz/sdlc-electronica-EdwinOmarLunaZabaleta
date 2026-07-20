# sdlc-electronica-EdwinOmarLunaZabaleta

# SDLC Electrónica: Semana 1

Este repositorio contiene las prácticas de la primera semana del curso, enfocadas en la transición de scripts a código de ingeniería mediante la aplicación rigurosa de control de versiones, tipado estático, testing automatizado y los principios de diseño SOLID.

## Descripción del Proyecto
El proyecto final es la reimplementación de un "Driver Modernizado" para UART. Se tomó una arquitectura monolítica tradicional de C (altamente acoplada) y se transformó en un sistema modular en Python que utiliza inyección de dependencias, parsers abstractos y configuración inmutable.

## Instalación y Configuración
1. Clonar el repositorio.
2. Crear un entorno virtual: `python3 -m venv .venv`
3. Activar el entorno: `source .venv/bin/activate`
4. Instalar las dependencias de desarrollo: `pip install pytest pytest-cov ruff mypy`

## Cómo correr los tests y validadores
Para ejecutar la suite de pruebas completa con reporte de cobertura (debe superar el 70%):
`pytest semana1/ -v --cov=semana1 --cov-report=term-missing`

Para ejecutar el linter (PEP 8):
`ruff check semana1/`

Para verificar el tipado estático:
`mypy semana1/ --ignore-missing-imports`

## Reflexión SOLID
La aplicación de los principios SOLID transformó por completo la testeabilidad del sistema. 
* **SRP:** Separar la configuración (`config.py`) del registro de datos (`recorder.py`) evitó que un error de escritura de archivo afectara la lógica de comunicación.
* **OCP e ISP:** Crear la abstracción `MessageParser` permite agregar nuevos protocolos (como CAN o I2C) sin modificar el código existente.
* **LSP y DIP:** Al inyectar el parser y la configuración en `UartDevice`, el hardware simulado ya no depende de implementaciones concretas. Esto permitió crear pruebas unitarias rápidas y 100% aisladas utilizando el patrón de diseño Mock y repositorios en memoria.
## Resultados Finales
Se logró un 100% de cobertura en el driver UART moderno tras aplicar técnicas TDG con GitHub Copilot.
