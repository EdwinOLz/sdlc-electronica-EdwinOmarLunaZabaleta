## Sprint 1 Planning

**Sprint Goal:** Construir el núcleo de procesamiento de datos y detección de anomalías del sistema IoT, permitiendo registrar lecturas, detectar valores fuera de umbral y emitir alertas abstractas.

**Historias seleccionadas (6):** US-01, US-02, US-03, US-04, US-05, US-06.

**Desglose de Tareas (Estimación < 4h):**
1. Crear dataclass `SensorReading` con validación de tipos (1h).
2. Crear clase `AnomalyDetector` que reciba umbrales en el constructor (1.5h).
3. Diseñar interfaz/clase base `AlertStrategy` (1h).
4. Implementar `ConsoleAlertStrategy` y `FileAlertStrategy` (1.5h).
5. Crear clase integradora `AlertManager` (1h).
6. Configurar tests con pytest garantizando >80% de cobertura (2h).

**Definition of Done (DoD):**
- Tests en Gherkin implementados en pytest.
- Cobertura >= 80%.
- Ruff y Mypy pasan sin errores.