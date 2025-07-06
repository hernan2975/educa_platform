# Referencia de Endpoints – API

## `/api/users/register/`
- `POST`: Registro de usuario (campos: username, email, password, is_premium)

## `/api/contents/`
- `GET`: Lista de cursos visibles según tipo de usuario (FREE o PREMIUM)

## `/api/stats/`
- `GET`: Estadísticas de uso (solo admin)

*Autenticación mediante token (a integrar más adelante con django-rest-auth o knox)*

