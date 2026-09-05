## Integrantes del Equipo

* **Camila Luna** - *DevOps & Integración Continua (CI/CD)*
* **Cristobal Sotelo** - *Desarrollo & Control de Versiones*
* **Gerardo Bustos** - *Pruebas & Documentación*

# Microservicio Python - Evaluación EP1 DevOps
---

##  Estrategia de Ramificación (GitFlow)
Elegimos **GitFlow** porque nos permite organizar el desarrollo usando distintas ramas sin hacer un desorden en el código:
- `Principal` (`main`): Se queda con la versión estable y limpia que sí funciona.
- `Desarrollar` (`develop`): Aquí juntamos todos los cambios que vamos haciendo el equipo.
- `feature/*`: Para crear y probar nuevas cosas sin romper el resto del proyecto.
- `hotfix/*`: Para arreglar fallos urgentes en producción de forma rápida.

Esta metodología nos ayuda a trabajar en equipo de manera más ordenada.

---

##  Convención de Commits
Usamos commits semánticos simples para saber qué hizo cada uno:
- `feat:` Para agregar nuevas funciones al microservicio.
- `fix:` Para corregir fallos en el código o en los tests.
- `ci:` Para los cambios en los flujos de GitHub Actions.
- `chore:` Para tareas de mantenimiento o actualizar librerías.

---

## Pipeline CI/CD
Dejamos todo automatizado con **GitHub Actions** (`.github/workflows/ci.yml`). Cada vez que subimos cambios con un `push` o `pull_request`, GitHub hace lo siguiente solo:
1. Monta el entorno con **Python 3.10**.
2. Instala las dependencias del archivo `requirements.txt`.
3. Corre las pruebas automatizadas con `pytest` para verificar que nada se rompa.

---

## Uso de Inteligencia Artificial
Usamos Inteligencia Artificial como un apoyo técnico para resolver errores en la terminal, solucionar problemas de permisos en Git y ayudarnos a estructurar la documentación.

---

##  Conclusión
Combinar GitFlow con el pipeline de GitHub Actions nos salvó de muchos errores. Probar el código automáticamente antes de unir las ramas hace que el trabajo sea mucho más fluido y seguro para todo el equipo.
