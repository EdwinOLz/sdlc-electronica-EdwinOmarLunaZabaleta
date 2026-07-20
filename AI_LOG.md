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