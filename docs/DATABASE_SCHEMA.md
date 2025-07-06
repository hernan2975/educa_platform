# 📊 Esquema de Base de Datos – Educa Platform

Este esquema resume los modelos principales del backend, sus campos y relaciones, para comprender la estructura de datos de la plataforma.

---

## 👤 `CustomUser` (users.models)
| Campo        | Tipo          | Descripción                         |
|--------------|---------------|-------------------------------------|
| id           | AutoField     | ID automático del usuario           |
| username     | CharField     | Nombre de usuario                   |
| email        | EmailField    | Correo electrónico                  |
| password     | CharField     | Contraseña hasheada                 |
| is_premium   | BooleanField  | Indica si el usuario es premium     |
| date_joined  | DateTimeField | Fecha de registro                   |

---

## 📚 `Course` (contents.models)
| Campo          | Tipo           | Descripción                                    |
|----------------|----------------|------------------------------------------------|
| id             | AutoField      | ID del curso                                  |
| title          | CharField      | Título del curso                              |
| description    | TextField      | Descripción del curso                         |
| image          | ImageField     | Imagen representativa                         |
| level_required | CharField      | FREE o PREMIUM                                |

🔗 **Relación**: Un curso puede tener muchos pictogramas (`1:N`)

---

## 🧩 `Pictogram` (contents.models)
| Campo        | Tipo          | Descripción                                         |
|--------------|---------------|-----------------------------------------------------|
| id           | AutoField     | ID del pictograma                                  |
| pictogram_id | CharField     | ID de referencia externa (ej: ARASAAC)             |
| caption      | CharField     | Texto o leyenda asociada al pictograma             |
| course       | ForeignKey    | Relación con el curso correspondiente (`M:1`)      |

---

## 📈 `UsageStats` (statistics.models)
| Campo          | Tipo            | Descripción                             |
|----------------|-----------------|-----------------------------------------|
| id             | AutoField       | ID del registro                         |
| user           | ForeignKey      | Usuario que accedió                     |
| course         | ForeignKey      | Curso accedido                          |
| last_access    | DateTimeField   | Último acceso del usuario al curso      |
| times_accessed | PositiveInteger | Número de veces que accedió             |

---

## 🔐 Relaciones clave

- Un usuario puede acceder a **muchos cursos**, pero el acceso a los cursos PREMIUM se limita mediante `is_premium`.
- Cada curso puede incluir múltiples pictogramas.
- Cada `UsageStats` vincula un usuario a un curso, registrando su actividad.

---

> Este esquema puede crecer fácilmente con más modelos, como comentarios, progresos, logros, etc. Te recomiendo mantenerlo actualizado para facilitar el trabajo colaborativo y la integración de funcionalidades nuevas.
