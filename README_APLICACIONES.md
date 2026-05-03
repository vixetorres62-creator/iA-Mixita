# IA-Mixita - Guía de Aplicaciones

Este proyecto incluye **4 formas diferentes** de usar IA-Mixita. Elige la que mejor se adapte a tus necesidades.

---

## 🚀 Opción 1: API Web (Flask)

### ¿Para qué sirve?
- Acceso desde cualquier navegador web
- Dashboard visual e intuitivo
- Perfecto para interfaces modernas

### ¿Cómo ejecutarla?

```bash
# 1. Instala solo Flask
pip install Flask

# 2. Ve a la carpeta de la app web
cd app_web

# 3. Ejecuta la aplicación
python app.py
```

### ¿Dónde accedo?
Abre tu navegador en: **http://localhost:5000**

### Funcionalidades:
- ✓ Ver información de la IA
- ✓ Ver estado del sistema
- ✓ Ver especialidades
- ✓ Desplegar módulos
- ✓ Resolver sistemas complejos
- ✓ Interfaz moderna y responsiva

---

## 🖥️ Opción 2: App de Escritorio (PyQt6)

### ¿Para qué sirve?
- Aplicación nativa tipo Windows/Mac
- Interfaz profesional con pestañas
- Funciona sin conexión a internet

### ¿Cómo ejecutarla?

```bash
# 1. Instala PyQt6
pip install PyQt6

# 2. Ve a la carpeta de la app
cd app_desktop

# 3. Ejecuta la aplicación
python app.py
```

### Funcionalidades:
- ✓ Pestañas para diferentes operaciones
- ✓ Información de la IA
- ✓ Despliegue de módulos
- ✓ Resolución de sistemas
- ✓ Interfaz moderna con tema personalizado
- ✓ Procesamiento sin bloqueos

---

## 💻 Opción 3: CLI Interactiva (Terminal)

### ¿Para qué sirve?
- Menú interactivo en la terminal
- La forma más rápida de usar
- Perfect para automatización

### ¿Cómo ejecutarla?

```bash
# 1. Ve a la carpeta de la app CLI
cd app_cli

# 2. Ejecuta la aplicación
python app.py
```

### Funcionalidades:
- ✓ Menú principal interactivo
- ✓ Ver información
- ✓ Ver especialidades
- ✓ Desplegar módulos (con sugerencias)
- ✓ Resolver sistemas (con contextos de ejemplo)
- ✓ Historial de operaciones
- ✓ 100% en terminal

### Ejemplo de uso:
```
1. Ver Información
2. Ver Especialidades
3. Desplegar Módulo
4. Resolver Sistema
5. Ver Historial
6. Salir
```

---

## 📦 Opción 4: Librería/Módulo Python

### ¿Para qué sirve?
- Usar IA-Mixita en tus propios proyectos
- Importar como módulo externo
- Reutilizable en múltiples proyectos

### ¿Cómo usarla?

```python
from ia_mixita import IAMixita

# Crear instancia
mixita = IAMixita()

# Obtener información
info = mixita.get_info()
print(info)

# Desplegar módulo
result = mixita.deploy_module("Blockchain & Tokens")
print(result)

# Resolver sistema
solution = mixita.solve_complex_system("Red Global")
print(solution)

# Obtener especialidades
specs = mixita.get_specialties()
print(specs)
```

---

## 📋 Estructura del Proyecto

```
iA-Mixita/
├── ia_mixita/                 # 📦 Librería principal
│   ├── __init__.py
│   └── core.py               # Clase IAMixita
│
├── app_web/                  # 🌐 API Web (Flask)
│   ├── app.py
│   └── templates/
│       └── index.html        # Dashboard web
│
├── app_desktop/              # 🖥️ App Escritorio (PyQt6)
│   └── app.py
│
├── app_cli/                  # 💻 CLI Interactiva
│   └── app.py
│
├── main.py                   # Script simple de prueba
├── requirements.txt          # Dependencias
└── README_APLICACIONES.md    # Este archivo
```

---

## 🔧 Instalación Rápida

### Solo para la API Web:
```bash
pip install -r requirements.txt
```

### Solo para la App de Escritorio:
```bash
pip install PyQt6
```

### Solo para CLI (sin dependencias extras):
```bash
# No requiere nada, solo Python 3.7+
```

### Para todo:
```bash
pip install -r requirements.txt
```

---

## 🎯 Recomendaciones

| Situación | Recomendación |
|-----------|--------------|
| Quiero una interfaz visual hermosa | **API Web** 🌐 |
| Quiero una app profesional tipo programa | **App Escritorio** 🖥️ |
| Quiero algo rápido y simple | **CLI Interactiva** 💻 |
| Quiero usar en mi código Python | **Librería** 📦 |
| Quiero todas las opciones | **Instala todo** ✨ |

---

## 🚀 Próximos pasos

1. **Elige una opción** según tus necesidades
2. **Instala las dependencias** necesarias
3. **Ejecuta la aplicación**
4. ¡**Disfruta usando IA-Mixita**!

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que Python 3.7+ está instalado
2. Revisa que las dependencias estén instaladas
3. Intenta ejecutar desde la carpeta correcta

---

¡Gracias por usar IA-Mixita! 🤖✨
