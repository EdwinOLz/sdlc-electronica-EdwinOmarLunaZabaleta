# Sprint Retrospective - Evaluación 1

## ¿Qué salió bien?
1. **Adopción de TDD:** Logré mantener una disciplina estricta con el ciclo Red-Green-Refactor, lo que me permitió alcanzar una cobertura de código global superior al 95%.
2. **Uso de Patrones de Diseño:** La implementación del patrón Strategy en el `AlertManager` hizo que el código sea altamente escalable y fácil de probar usando `MagicMock`.
3. **Calidad Automatizada:** La configuración inicial con `pyproject.toml` funcionó como una excelente red de seguridad, obligándome a mantener un tipado estricto (Mypy) y un formato limpio (Ruff).

## ¿Qué se puede mejorar?
1. **Estimación de tiempo:** Al inicio hubo un ligero cruce de conceptos entre las herramientas de IA y los requerimientos estrictos de tipado, lo que requirió retrabajo manual.
2. **Redacción de Historias:** Identifiqué el anti-patrón de escribir historias de usuario "Para el sistema" y aprendí a asignarles roles reales que aporten valor.

## Acción concreta para el próximo Sprint
* **Revisión temprana de Mypy:** Antes de ejecutar las pruebas lógicas (`pytest`), correré las validaciones estáticas (`ruff` y `mypy`) en cada commit para evitar acumular errores de formato o tipado al final del desarrollo.