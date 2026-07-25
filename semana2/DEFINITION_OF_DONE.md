# Definition of Done (DoD)

Para que una Historia de Usuario o tarea se considere completamente terminada (Done) en este proyecto, debe cumplir obligatoriamente con los siguientes criterios:

- [ ] **Criterios Gherkin automatizados:** Todos los escenarios definidos (Given, When, Then) en la historia de usuario están implementados y pasando exitosamente como tests en `pytest`.
- [ ] **Cobertura de código mínima:** El reporte de `pytest` demuestra una cobertura de pruebas igual o superior al **80%**.
- [ ] **Linter limpio (Ruff):** La ejecución de `ruff` pasa sin advertencias ni errores, respetando las reglas de formato y calidad (E, F, I, UP, B).
- [ ] **Tipado estricto limpio (Mypy):** La ejecución de `mypy` pasa sin errores, asegurando que todas las funciones tienen sus tipos definidos (`disallow_untyped_defs`).
- [ ] **Auto-revisión (Pull Request):** El código no se subió directamente a la rama principal (main). Se creó un Pull Request y el autor leyó el *diff* línea por línea antes de aceptar la integración (merge).
- [ ] **Documentación actualizada:** Cualquier cambio en la lógica o en los requisitos ha sido reflejado en la documentación correspondiente del proyecto.