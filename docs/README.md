 # Educa Platform – Documentación

Este proyecto tiene como objetivo desarrollar una plataforma educativa tipo freemium, accesible e inclusiva, usando Django, DRF y APIs externas como ARASAAC.

## Estructura del backend

- `users/` → Registro, login y roles de usuario
- `contents/` → Cursos, pictogramas, niveles de acceso
- `statistics/` → Registro de accesos y visualización de métricas

## Ramas principales

| Rama                    | Propósito                                                  |
|-------------------------|------------------------------------------------------------|
| `main`                  | Versión estable para producción                            |
| `dev`                   | Rama de integración y pruebas continuas                    |
| `feature/backend-init`  | Estructura inicial del backend Django                      |
| `feature/models-users`  | Modelos de usuario, autenticación y registro               |
| `feature/courses`       | CRUD de cursos y restricción de contenido premium          |
| `feature/api-arasaac`   | Integración con la API de pictogramas de ARASAAC           |
| `feature/tts`           | Generación de voz (gTTS o API externa)                     |
| `feature/admin-panel`   | Estadísticas y visualizaciones para el panel de administración |
| `feature/frontend-base` | Plantilla HTML/CSS accesible y responsive                  |
| `hotfix/fix-login`      | Corrección urgente en autenticación o seguridad            |
