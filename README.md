## Integrantes del Equipo

* **Camila Luna** - *DevOps & Integración Continua (CI/CD)*
* **Cristobal Sotelo** - *Desarrollo & Control de Versiones*
* **Gerardo Bustos** - *Pruebas & Documentación*
  # Microservicio Estudiantes - Evaluación Parcial 2 (EP2)

## Información del Proyecto
- **Asignatura:** Ingeniería DevOps (DOY0101)
- **Institución:** Duoc UC
- **Repositorio:** `microservicio-estudiantes`
- **Lenguaje / Framework:** Python (`pytest`)

---

## Arquitectura y Orquestación
- **Contenedorización:** Se definió un `Dockerfile` optimizado sobre `python:3.10-slim`.
- **Orquestación:** Se configuró un entorno multicontenedor simulado utilizando `docker-compose.yml`.

---

## Estrategia de Ramificación (GitFlow)
El desarrollo del proyecto se lleva a cabo mediante la rama principal de integración:
- `desarrollar`: Rama donde se integran y prueban los cambios antes del despliegue final.

---

## Pipeline CI/CD (GitHub Actions)
El pipeline automatizado (`.github/workflows/ci.yml`) consta de las siguientes etapas:
1. **Tests Unitarios:** Ejecución automatizada de pruebas mediante `pytest`.
2. **Análisis de Seguridad (SAST):** Escaneo de vulnerabilidades en dependencias mediante **Snyk**.
3. **Construcción y Despliegue:** Creación de la imagen Docker y prueba de orquestación con `docker compose`.

---

## Declaración sobre el uso de Inteligencia Artificial
Se utilizó IA como herramienta de apoyo exclusivamente para:
- Formateo y corrección de sintaxis en archivos YAML (`ci.yml` y `docker-compose.yml`).
- Estructuración y diagramación del archivo de documentación `README.md`.

