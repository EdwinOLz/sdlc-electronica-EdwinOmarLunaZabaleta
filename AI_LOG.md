# Bitácora de IA - Curso SDLC

## Semana 1
### Entrada 1 - Día 1: Comprensión de inmutabilidad y f-strings
*   **Herramientas usadas:** GitHub Copilot (autocompletado) y Gemini Chat (tutoría conceptual).
*   **Prompt/Situación:** Copilot me sugería código para las funciones (como usar f-strings para JSON o comparaciones encadenadas), pero como generaba el código sin explicación, usé Gemini Chat para que me explicara el concepto de inmutabilidad en clases `@dataclass(frozen=True)` antes de aceptar las sugerencias de Copilot.
*   **Mi decisión:** Acepté la sugerencia de Copilot para la función `a_json` pero decidí escribir manualmente `calibrar_offset` basándome en la explicación de Gemini para asegurar que estaba devolviendo un objeto nuevo en lugar de mutarlo.
*   **Reflexión:** Necesitaba entender que `r.sensor_type.name` se usa para extraer la cadena limpia del Enum, y que al ser un objeto "congelado", Python prohíbe reasignar `r.value`. Usar el chat conversacional con gemini me permitió entender, en lugar de solo aceptar el autocompletado a ciegas.
*   **puntos extra:** Aunque Copilot sugirió formas más "limpias" de una sola línea para las validaciones lógicas, decidí mantener la estructura clásica con `if` y `else`. A mi parecer, es una estructura más ordenada y permite hacer *debug* de las variables de manera más sencilla al poner puntos de interrupción en caso de que el código llegase a fallar.

### Entrada 2 - Día 2: Tests automáticos para la Máquina de Estados (FSM)
*   **Herramientas usadas:** GitHub Copilot (Agente/Chat).
*   **Prompt/Situación:** Le pedí a Copilot: "necesito generar 4 test para el archivo fsm_demo.py donde se valide el estado inicial del sistema, la transicion de rojo a verde, el ciclo completo que vuelve a rojo, y el conteo de los ciclos".
*   **Sugerencia de la IA:** Copilot generó las 4 funciones de test correctamente usando `pytest`. En su proceso interno, la IA intentó reescribir el archivo `fsm_demo.py` en la terminal para asegurarse de que estuviera completo antes de correr las pruebas. Finalmente, ejecutó los tests de forma automática y los 4 pasaron.
*   **Mi decisión:** Acepté los tests generados porque cubren exactamente lo solicitado. Comprobé que el archivo `fsm_demo.py` no sufrió alteraciones lógicas, ya que la IA simplemente inyectó la misma estructura que yo ya había desarrollado previamente.
*   **Reflexión:** Verifiqué que el código de los tests sigue el patrón Arrange-Act-Assert. Entiendo que leer la variable protegida `fsm._cycle_count` directamente en el último test es válido en este contexto, ya que en pruebas unitarias es necesario inspeccionar el estado interno para verificar la mecánica correcta de la máquina de estados.

### Entrada 3 - Día 3: Implementación de Principios SOLID (SRP, OCP, LSP) y Testing con Mocks
*   **Herramientas usadas:** GitHub Copilot (Agente).
*   **Prompt/Situación:** Necesitaba generar 2 tests para el archivo `solid_srp_ocp_lsp.py`: uno para comprobar que el mensaje se envía al superar el umbral y otro para cuando no se supera.
*   **Sugerencia de la IA:** Copilot implementó un patrón de prueba superior al esperado. En lugar de leer salidas de consola, creó una clase `FakeAlert` (un objeto espía/mock) que almacena los mensajes en una lista interna. Luego inyectó esta alerta falsa en el detector. Durante el proceso, el agente se confundió temporalmente con el estado del archivo en el disco e intentó reescribirlo por terminal, pero finalmente corrigió su propio contexto y ejecutó las pruebas con éxito.
*   **Mi decisión:** Acepté la estrategia de `FakeAlert` porque es una demostración excelente del principio LSP (Liskov Substitution Principle).
*   **Reflexión:** El test demuestra que gracias a que el código está desacoplado, puedo inyectar un objeto falso exclusivo para pruebas sin tener que modificar ni una sola línea del `AnomalyDetector`. Esto aísla el comportamiento matemático del detector de las operaciones lentas o ruidosas (como enviar correos reales o imprimir en consola).

### Entrada 4 - Día 4: Principios SOLID (ISP y DIP) y Testing
*   **Herramientas usadas:** GitHub Copilot.
*   **Prompt/Situación:** Necesitaba generar 2 tests con `pytest` para validar la Segregación de Interfaces (ISP) y la Inversión de Dependencias (DIP) en el archivo `solid_isp_dip.py`. Le di a Copilot instrucciones exactas sobre qué clases instanciar (`SensorSimple`, `InMemoryRepository`, `DataProcessor`).
*   **Sugerencia de la IA:** Copilot generó las pruebas con la sintaxis correcta. Para el test de DIP, instanció el repositorio falso en memoria, lo inyectó en el procesador y verificó que el objeto inmutable `SensorReading` se almacenara y recuperara correctamente.
*   **Mi decisión:** Acepté la generación porque las pruebas validan exitosamente que el código está desacoplado de dependencias concretas y de interfaces infladas.
*   **Reflexión:** Este ejercicio me demostró el valor real de DIP a la hora de hacer pruebas. Al depender de una abstracción (`Protocol`), pude engañar al `DataProcessor` inyectándole una base de datos falsa (`InMemoryRepository`) en lugar de tener que configurar una conexión real a PostgreSQL. Esto hace que mis pruebas corran en milisegundos y sean 100% confiables.

### Entrada 5 - Día 5: Ejercicio Integrador "El Driver Modernizado" (TDG)
*   **Herramientas usadas:** GitHub Copilot.
*   **Prompt/Situación:** Apliqué Test-Driven Generation (TDG). Escribí únicamente las firmas de las funciones y los docstrings detallados para las pruebas de `config`, `parsers`, `device` y `recorder`, dejando que el agente autocompletara la implementación.
*   **Sugerencia de la IA:** Copilot generó implementaciones muy precisas. Utilizó `pytest.raises` para verificar el manejo de errores (como el `FrozenInstanceError` en el config y `RuntimeError` en el dispositivo) y `tmp_path` de pytest para aislar las pruebas de escritura de archivos JSON.
*   **Mi decisión:** Acepté las sugerencias casi en su totalidad. El único cambio que realicé manualmente fue corregir la sintaxis de las aserciones booleanas en los parsers (cambiando `assert algo == True` por `assert algo`), siguiendo las advertencias del linter `ruff` para cumplir con PEP 8.
*   **Reflexión:** Escribir primero el docstring me forzó a pensar en el comportamiento esperado, en lugar de perderme escribiendo líneas repetitivas de código. Dividir el driver monolítico con SOLID permitió que cada clase fuera probada de forma 100% aislada.

## Semana 2 
### Entrada 1: Auditoría de Historias de Usuario con IA

**Prompt:** "IA como crítica: audita mis Gherkin para US-01 (Registrar lectura) y US-02 (Alerta de problema). ¿Es verificable? ¿es ambiguo? ¿qué caso borde falta? También revisa mis dudas sobre la complejidad y el SRP."

**Qué produjo la IA:**
La IA señaló aciertos y varios defectos críticos en la redacción orientada a pruebas (TDD):
1. Para US-01: Sugirió separar la historia de "guardar datos" de la de "consultar historiales" y detectó la falta de casos borde para datos físicamente imposibles (ej. -500 C) y payloads malformados.
2. Para US-02: Encontró un paso no programable/inverificable ("And puedo atender un posible problema"). 
3. Detectó falta de manejo de histéresis/rebotes en US-02 (señales que oscilan justo en el límite del threshold).
4. Me ayudó a aclarar cómo aplicar SRP: la US-02 no debe preocuparse de verificar si el sensor existe, porque de eso ya se encargó la capa anterior (US-01).

**Reflexión:**
me parecen muy acertadas las siguerencias realizadas por la IA ya que contempla casos que yo habia ignorado asi como tambien me hizo notar errores en mi Gherkin como casos no programables los cuales no note por mi cuenta y me ayudo a resolver mis dudas con el principio de responsabilidad unica o srp que podia llevarme a generar codigo caotico ignorando totalmente este principio por no separar modulos