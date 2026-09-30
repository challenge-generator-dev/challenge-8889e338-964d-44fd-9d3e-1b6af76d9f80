# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `tests/test_input_validator.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/test_interest_calculator.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Hacer un programa simple con Python

### Reto
- Tema: Programación básica con enfoque en lógica y resolución de problemas
- Seniority: trainee-l1
- Tipo: practical
- Título: Creación de un programa simple en Python
- Tiempo estimado: 2 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición de requerimientos y entrada de datos — objetivo: Establecer los requerimientos del programa y asegurar que los datos de entrada sean válidos — entregable (NO resolver): Programa que solicita y valida la entrada de datos.
- Fase 2: Cálculo del interés simple — objetivo: Implementar la lógica para calcular el interés simple y el monto total a pagar — entregable (NO resolver): Programa que calcula y muestra el interés simple y el monto total a pagar.
- Fase 3: Mejora y pruebas del programa — objetivo: Mejorar el programa para manejar más casos de error y realizar pruebas exhaustivas — entregable (NO resolver): Programa mejorado con manejo de errores adicionales y pruebas realizadas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
pytest==8.1.1

// === ARCHIVO: src/main.py ===
"""
Programa para calcular el interés simple de un préstamo.
Solicita al usuario el monto del préstamo, la tasa de interés anual y el tiempo en años,
valida las entradas y calcula el interés ganado y el monto total a pagar.
"""

import sys
from validators.input_validator import validate_loan_inputs
from calculators.interest_calculator import calculate_simple_interest
from utils.error_messages import INPUT_ERROR_MESSAGE

def main():
    """Función principal que coordina la entrada, validación y cálculo."""
    print("=== Calculadora de Interés Simple ===")
    
    try:
        # Solicitar datos al usuario
        principal = float(input("Ingrese el monto del préstamo: $"))
        rate = float(input("Ingrese la tasa de interés anual (%): "))
        time = float(input("Ingrese el tiempo en años: "))
        
        # Validar entradas
        validate_loan_inputs(principal, rate, time)
        
        # Calcular interés y monto total
        interest, total_amount = calculate_simple_interest(principal, rate, time)
        
        # Mostrar resultados
        print(f"\nInterés ganado: ${interest:.2f}")
        print(f"Monto total a pagar: ${total_amount:.2f}")
        
    except ValueError as ve:
        print(f"\nError: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError inesperado: {INPUT_ERROR_MESSAGE}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

// === ARCHIVO: __init__.py ===
"""
Módulo principal del Calculador de Interés Simple.

Este paquete proporciona funcionalidades para calcular el interés simple
de préstamos financieros, con validación robusta de entradas y manejo
de errores descriptivo.

Paquetes incluidos:
    - src.validators: Validación de entradas del usuario
    - src.calculators: Cálculo de interés simple
    - src.utils: Utilidades y manejo de errores
"""

import sys
from typing import Optional, Tuple
from decimal import Decimal

# Constantes de configuración global del módulo
VERSION = "1.0.0"
NOMBRE_PROGRAMA = "Calculador de Interés Simple"
DESCRIPCION_PROGRAMA = "Herramienta para calcular el interés simple de préstamos financieros"

# Valores por defecto para cálculos
TASA_MINIMA = Decimal("0.0")
TASA_MAXIMA = Decimal("100.0")
MONTO_MINIMO = Decimal("0.01")
TIEMPO_MINIMO = Decimal("0.0")
TIEMPO_MAXIMO = Decimal("50.0")

# Formato de salida
FORMATO_DECIMAL = "{:.2f}"
MENSAJE_BIENVENIDA = """
========================================
{} - v{}
{}
========================================
""".format(NOMBRE_PROGRAMA, VERSION, DESCRIPCION_PROGRAMA)

# Códigos de salida del programa
EXIT_SUCCESS = 0
EXIT_ERROR_INPUT = 1
EXIT_ERROR_CALCULO = 2
EXIT_ERROR_DESCONOCIDO = 3

def obtener_version() -> str:
    """
    Retorna la versión actual del programa.
    
    Returns:
        str: Versión del programa en formato semántico
    """
    return VERSION

def obtener_info_programa() -> Tuple[str, str, str]:
    """
    Retorna información básica del programa.
    
    Returns:
        Tuple[str, str, str]: Tupla con (nombre, versión, descripción)
    """
    return (NOMBRE_PROGRAMA, VERSION, DESCRIPCION_PROGRAMA)

def mostrar_bienvenida() -> None:
    """Imprime el mensaje de bienvenida del programa."""
    print(MENSAJE_BIENVENIDA)

def obtener_codigo_salida(tipo_error: str) -> int:
    """
    Retorna el código de salida apropiado según el tipo de error.
    
    Args:
        tipo_error: Tipo de error ocurrido ('input', 'calculo', 'desconocido')
    
    Returns:
        int: Código de salida del sistema
    """
    codigos = {
        "input": EXIT_ERROR_INPUT,
        "calculo": EXIT_ERROR_CALCULO,
        "desconocido": EXIT_ERROR_DESCONOCIDO
    }
    return codigos.get(tipo_error, EXIT_ERROR_DESCONOCIDO)

def configurarLocale() -> None:
    """
    Configura el locale para formateo de números.
    
    Asegura que el separador decimal sea el punto para
    compatibilidad con los cálculos.
    """
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        pass

def inicializar_modulo() -> None:
    """
    Inicializa el módulo configurando el entorno.
    
    Esta función debe llamarse al inicio del programa
    para asegurar que todos los componentes estén
    correctamente configurados.
    """
    configurarLocale()
    mostrar_bienvenida()

def validar_rango_tasa(tasa: Decimal) -> bool:
    """
    Valida que la tasa de interés esté en el rango permitido.
    
    Args:
        tasa: Tasa de interés a validar
    
    Returns:
        bool: True si la tasa es válida
    """
    return TASA_MINIMA <= tasa <= TASA_MAXIMA

def validar_rango_monto(monto: Decimal) -> bool:
    """
    Valida que el monto del préstamo sea válido.
    
    Args:
        monto: Monto del préstamo a validar
    
    Returns:
        bool: True si el monto es válido
    """
    return monto >= MONTO_MINIMO

def validar_rango_tiempo(tiempo: Decimal) -> bool:
    """
    Valida que el tiempo en años esté en el rango permitido.
    
    Args:
        tiempo: Tiempo en años a validar
    
    Returns:
        bool: True si el tiempo es válido
    """
    return TIEMPO_MINIMO <= tiempo <= TIEMPO_MAXIMO

def formatear_moneda(valor: Decimal) -> str:
    """
    Formatea un valor decimal como moneda.
    
    Args:
        valor: Valor a formatear
    
    Returns:
        str: Valor formateado con símbolo de moneda
    """
    return f"${FORMATO_DECIMAL.format(valor)}"

def formatear_porcentaje(valor: Decimal) -> str:
    """
    Formatea un valor decimal como porcentaje.
    
    Args:
        valor: Valor a formatear (ej: 0.05 para 5%)
    
    Returns:
        str: Porcentaje formateado
    """
    return f"{FORMATO_DECIMAL.format(valor * 100)}%"

def obtener_limites() -> dict:
    """
    Retorna un diccionario con los límites de validación.
    
    Returns:
        dict: Diccionario con límites de tasa, monto y tiempo
    """
    return {
        "tasa_minima": TASA_MINIMA,
        "tasa_maxima": TASA_MAXIMA,
        "monto_minimo": MONTO_MINIMO,
        "tiempo_minimo": TIEMPO_MINIMO,
        "tiempo_maximo": TIEMPO_MAXIMO
    }

def verificar_entorno() -> bool:
    """
    Verifica que el entorno de ejecución sea el adecuado.
    
    Returns:
        bool: True si el entorno es válido
    """
    return sys.version_info >= (3, 8)

def obtener_info_python() -> str:
    """
    Retorna información sobre la versión de Python.
    
    Returns:
        str: Información de versión
    """
    return f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

def ejecutar_inicio() -> None:
    """
    Ejecuta la secuencia de inicio del programa.
    
    Verifica el entorno, muestra la bienvenida e informa
    sobre la versión de Python en uso.
    """
    if not verificar_entorno():
        print("Advertencia: Se recomienda Python 3.8 o superior")
    
    inicializar_modulo()
    print(f"Entorno: {obtener_info_python()}")
    print()

// === ARCHIVO: README.md ===
# Calculador de Interés Simple

## Descripción

Este programa calcula el interés simple de un préstamo financiero. Dados el monto del préstamo, la tasa de interés anual y el tiempo en años, el programa determina el interés ganado y el monto total a pagar.

## Requisitos

- Python 3.8 o superior
- pytest 8.1.1 (para ejecutar las pruebas)

## Instalación

1. Asegúrate de tener Python instalado:
   ```bash
   python --version
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

### Modo interactivo
Ejecuta el programa sin argumentos para introducir los datos manualmente:

```bash
python -m src.main
```

El programa te solicitará:
1. **Monto del préstamo**: Ingresa el monto en dólares (ej: 1000)
2. **Tasa de interés anual**: Ingresa la tasa en porcentaje (ej: 5 para 5%)
3. **Tiempo en años**: Ingresa el período del préstamo (ej: 2)

### Ejemplo de ejecución

```
========================================
Calculador de Interés Simple - v1.0.0
Herramienta para calcular el interés simple de préstamos financieros
========================================

Ingrese el monto del prestamo: 1000
Ingrese la tasa de interes anual (%): 5
Ingrese el tiempo en anos: 2

========================================
RESULTADOS DEL CÁLCULO
========================================
Monto del prestamo: $1000.00
Tasa de interes: 5.00%
Tiempo: 2 anos
--------------------------------------
Interes simple generado: $100.00
Monto total a pagar: $1100.00
========================================
```

### Validaciones de entrada

El programa valida los siguientes casos de error:

| Caso | Entrada | Resultado |
|------|---------|-----------|
| Monto negativo | -500 | Error: El monto no puede ser negativo |
| Monto cero | 0 | Error: El monto debe ser mayor a cero |
| Tasa mayor al 100% | 150 | Error: La tasa no puede exceder el 100% |
| Tasa negativa | -5 | Error: La tasa no puede ser negativa |
| Tiempo negativo | -1 | Error: El tiempo no puede ser negativo |
| Tiempo excesivo | 100 | Error: El tiempo máximo es 50 años |
| Entrada no numérica | abc | Error: Debe ingresar un número válido |

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest tests/ -v
```

Para ejecutar pruebas específicas:

```bash
# Probar solo el validador de entrada
pytest tests/test_input_validator.py -v

# Probar solo el calculador de interés
pytest tests/test_interest_calculator.py -v
```

## Estructura del Proyecto

```
proyecto/
├── __init__.py              # Punto de entrada del paquete
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Este archivo
├── src/
│   ├── __init__.py          # Paquete src
│   ├── main.py              # Punto de entrada del programa
│   ├── validators/
│   │   └── input_validator.py   # Validación de entradas
│   ├── calculators/
│   │   └── interest_calculator.py  # Cálculo de interés
│   └── utils/
│       └── error_messages.py     # Mensajes de error
└── tests/
    ├── test_input_validator.py
    └── test_interest_calculator.py
```

## Fórmula del Interés Simple

El interés simple se calcula mediante la fórmula:

```
I = P × r × t
```

Donde:
- **I**: Interés simple
- **P**: Capital o monto principal
- **r**: Tasa de interés anual (en decimal)
- **t**: Tiempo en años

El monto total a pagar es:

```
Monto Total = P + I
```

## Licencia

Este proyecto es con fines educativos.

// === ARCHIVO: src/__init__.py ===
"""
Paquete principal del código fuente.

Este módulo contiene la lógica central del calculador de interés simple,
organizada en subpaquetes especializados para validación, cálculo y
utilidades comunes.
"""

import os
import sys
from pathlib import Path
from typing import List, Optional

# Definición de la ruta base del proyecto
RUTA_PROYECTO = Path(__file__).parent.parent
RUTA_SRC = Path(__file__).parent
RUTA_TESTS = RUTA_PROYECTO / "tests"

def obtener_ruta_proyecto() -> Path:
    """
    Retorna la ruta raíz del proyecto.
    
    Returns:
        Path: Ruta absoluta del directorio del proyecto
    """
    return RUTA_PROYECTO

def obtener_ruta_src() -> Path:
    """
    Retorna la ruta del directorio src.
    
    Returns:
        Path: Ruta absoluta del directorio src
    """
    return RUTA_SRC

def verificar_estructura_directorios() -> bool:
    """
    Verifica que la estructura de directorios requerida exista.
    
    Returns:
        bool: True si la estructura es válida
    """
    directorios_requeridos = [
        RUTA_SRC / "validators",
        RUTA_SRC / "calculators",
        RUTA_SRC / "utils",
        RUTA_TESTS
    ]
    
    for directorio in directorios_requeridos:
        if not directorio.exists():
            return False
    return True

def crear_directorios_si_no_existen() -> None:
    """
    Crea los directorios necesarios si no existen.
    
    Esta función asegura que la estructura de carpetas
    del proyecto esté disponible para el funcionamiento
    correcto del programa.
    """
    directorios = [
        RUTA_SRC / "validators",
        RUTA_SRC / "calculators",
        RUTA_SRC / "utils",
        RUTA_TESTS
    ]
    
    for directorio in directorios:
        directorio.mkdir(parents=True, exist_ok=True)

def listar_modulos_disponibles() -> List[str]:
    """
    Lista los módulos disponibles en el paquete src.
    
    Returns:
        List[str]: Nombres de los submódulos disponibles
    """
    modulos = []
    
    for item in RUTA_SRC.iterdir():
        if item.is_file() and item.suffix == ".py" and item.name != "__init__.py":
            modulos.append(item.stem)
        elif item.is_dir() and (item / "__init__.py").exists():
            modulos.append(item.name)
    
    return sorted(modulos)

def importar_modulo(nombre_modulo: str):
    """
    Importa un módulo dinámicamente por su nombre.
    
    Args:
        nombre_modulo: Nombre del módulo a importar
    
    Returns:
        Módulo importado
    
    Raises:
        ImportError: Si el módulo no existe
    """
    try:
        return __import__(f"src.{nombre_modulo}", fromlist=["*"])
    except ImportError as e:
        raise ImportError(f"No se pudo importar el módulo '{nombre_modulo}': {e}")

def obtener_ruta_absoluta(relativo: str) -> Path:
    """
    Convierte una ruta relativa a absoluta basada en la raíz del proyecto.
    
    Args:
        relativo: Ruta relativa desde la raíz del proyecto
    
    Returns:
        Path: Ruta absoluta
    """
    return RUTA_PROYECTO / relativo

def verificar_archivo_existe(ruta: str) -> bool:
    """
    Verifica si un archivo existe en el proyecto.
    
    Args:
        ruta: Ruta del archivo a verificar
    
    Returns:
        bool: True si el archivo existe
    """
    return (RUTA_PROYECTO / ruta).exists()

def obtener_configuracion_ejecucion() -> dict:
    """
    Retorna la configuración de ejecución del programa.
    
    Returns:
        dict: Diccionario con configuración
    """
    return {
        "ruta_proyecto": str(RUTA_PROYECTO),
        "ruta_src": str(RUTA_SRC),
        "ruta_tests": str(RUTA_TESTS),
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "plataforma": sys.platform
    }

def mostrar_info_configuracion() -> None:
    """
    Imprime información de configuración del entorno.
    
    Útil para depuración y para verificar que el
    entorno está correctamente configurado.
    """
    config = obtener_configuracion_ejecucion()
    
    print("Configuración del entorno de ejecución:")
    print(f"  Ruta del proyecto: {config['ruta_proyecto']}")
    print(f"  Ruta src: {config['ruta_src']}")
    print(f"  Ruta tests: {config['ruta_tests']}")
    print(f"  Python: {config['python_version']}")
    print(f"  Plataforma: {config['plataforma']}")
    print()
    print("Módulos disponibles:")
    for modulo in listar_modulos_disponibles():
        print(f"  - {modulo}")

def validar_ambiente() -> bool:
    """
    Valida que el ambiente esté correctamente configurado.
    
    Returns:
        bool: True si el ambiente es válido
    """
    if sys.version_info < (3, 8):
        print("Error: Se requiere Python 3.8 o superior")
        return False
    
    if not verificar_estructura_directorios():
        print("Advertencia: Estructura de directorios incompleta. Intentando crear...")
        crear_directorios_si_no_existen()
    
    return True

def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación verificando el entorno.
    
    Esta función prepara todo lo necesario para
    que el programa pueda ejecutarse correctamente.
    """
    if not validar_ambiente():
        sys.exit(1)
    
    print("Entorno validado correctamente.")
    print()


// === ARCHIVO: src/validators/input_validator.py ===
"""Módulo de validación de datos de entrada para el cálculo de interés simple.

Este módulo contiene funciones puras que verifican la validez de los
parámetros de entrada: monto del préstamo, tasa de interés y tiempo en años.
"""

from decimal import Decimal, InvalidOperation
from typing import Union


class ValidationError(Exception):
    """Excepción personalizada para errores de validación de entrada."""
    
    def __init__(self, message: str, field: str = "unknown"):
        self.field = field
        super().__init__(message)


def validate_positive_amount(amount: Union[int, float, str, Decimal]) -> Decimal:
    """Valida que el monto del préstamo sea un valor positivo.
    
    Args:
        amount: El monto del préstamo a validar. Puede ser int, float, str o Decimal.
    
    Returns:
        Decimal: El monto validado como Decimal.
    
    Raises:
        ValidationError: Si el monto es negativo, cero o no es numérico.
    """
    try:
        decimal_amount = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError(
            f"El monto debe ser un valor numérico válido. Valor recibido: {amount}",
            field="amount"
        ) from e
    
    if decimal_amount <= 0:
        raise ValidationError(
            f"El monto del préstamo debe ser positivo. Valor recibido: {amount}",
            field="amount"
        )
    
    return decimal_amount


def validate_interest_rate(rate: Union[int, float, str, Decimal]) -> Decimal:
    """Valida que la tasa de interés esté en un rango válido (0-100%).
    
    La tasa debe expresarse como porcentaje (ej. 5 para 5%) y se convierte
    a decimal para cálculos internos.
    
    Args:
        rate: La tasa de interés anual a validar.
    
    Returns:
        Decimal: La tasa validada como Decimal.
    
    Raises:
        ValidationError: Si la tasa es negativa o mayor al 100%.
    """
    try:
        decimal_rate = Decimal(str(rate))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError(
            f"La tasa de interés debe ser un valor numérico válido. Valor recibido: {rate}",
            field="interest_rate"
        ) from e
    
    if decimal_rate < 0:
        raise ValidationError(
            f"La tasa de interés no puede ser negativa. Valor recibido: {rate}",
            field="interest_rate"
        )
    
    if decimal_rate > 100:
        raise ValidationError(
            f"La tasa de interés no puede exceder el 100%. Valor recibido: {rate}",
            field="interest_rate"
        )
    
    return decimal_rate


def validate_years(years: Union[int, float, str]) -> int:
    """Valida que el tiempo en años sea un valor entero positivo.
    
    Args:
        years: El tiempo en años a validar.
    
    Returns:
        int: El tiempo validado como entero positivo.
    
    Raises:
        ValidationError: Si el tiempo no es un número positivo o es cero.
    """
    try:
        numeric_years = float(years)
    except (ValueError, TypeError) as e:
        raise ValidationError(
            f"El tiempo en años debe ser un valor numérico válido. Valor recibido: {years}",
            field="years"
        ) from e
    
    if numeric_years <= 0:
        raise ValidationError(
            f"El tiempo en años debe ser positivo. Valor recibido: {years}",
            field="years"
        )
    
    if not numeric_years.is_integer():
        raise ValidationError(
            f"El tiempo en años debe ser un número entero. Valor recibido: {years}",
            field="years"
        )
    
    return int(numeric_years)


def validate_all_inputs(amount, rate, years):
    """Valida todos los parámetros de entrada simultáneamente.
    
    Esta función orchestrar valida cada parámetro y retorna una tupla
    con los valores validados listos para cálculo.
    
    Args:
        amount: Monto del préstamo.
        rate: Tasa de interés anual.
        years: Tiempo en años.
    
    Returns:
        tuple: (amount_decimal, rate_decimal, years_int) validados.
    
    Raises:
        ValidationError: Si cualquier parámetro es inválido.
    """
    validated_amount = validate_positive_amount(amount)
    validated_rate = validate_interest_rate(rate)
    validated_years = validate_years(years)
    
    return validated_amount, validated_rate, validated_years


// === ARCHIVO: src/calculators/interest_calculator.py ===
"""Módulo de cálculo de interés simple para préstamos financieros.

Implementa la fórmula estándar del interés simple: I = P * r * t
donde:
    I = Interés generado
    P = Principal (monto del préstamo)
    r = Tasa de interés anual (en formato decimal)
    t = Tiempo en años

Este módulo utiliza Decimal para evitar errores de precisión con números flotantes.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Union


class CalculationError(Exception):
    """Excepción personalizada para errores en cálculos financieros."""
    
    def __init__(self, message: str):
        super().__init__(message)


def convert_rate_to_decimal(rate_percent: Union[int, float, str, Decimal]) -> Decimal:
    """Convierte la tasa de interés de porcentaje a formato decimal.
    
    La tasa se ingresa como porcentaje (ej. 5 para 5%) y se convierte
    a decimal (0.05) para usar en la fórmula del interés.
    
    Args:
        rate_percent: Tasa de interés en formato porcentaje.
    
    Returns:
        Decimal: La tasa en formato decimal para cálculos.
    """
    rate_str = str(rate_percent)
    decimal_rate = Decimal(rate_str)
    
    return decimal_rate / Decimal('100')


def calculate_simple_interest(
    principal: Decimal,
    rate_percent: Decimal,
    years: int
) -> Decimal:
    """Calcula el interés simple generado por un préstamo.
    
    Fórmula: I = P * r * t
    
    Args:
        principal: Monto principal del préstamo (Decimal).
        rate_percent: Tasa de interés anual en porcentaje (Decimal).
        years: Tiempo en años (int).
    
    Returns:
        Decimal: El interés simple calculado, redondeado a 2 decimales.
    """
    if not isinstance(principal, Decimal):
        principal = Decimal(str(principal))
    
    if not isinstance(rate_percent, Decimal):
        rate_percent = Decimal(str(rate_percent))
    
    rate_decimal = convert_rate_to_decimal(rate_percent)
    
    interest = principal * rate_decimal * Decimal(str(years))
    
    return interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_total_amount(
    principal: Decimal,
    rate_percent: Decimal,
    years: int
) -> Decimal:
    """Calcula el monto total a pagar incluyendo principal más interés.
    
    Fórmula: Total = P + I = P + (P * r * t)
    
    Args:
        principal: Monto principal del préstamo (Decimal).
        rate_percent: Tasa de interés anual en porcentaje (Decimal).
        years: Tiempo en años (int).
    
    Returns:
        Decimal: El monto total a pagar, redondeado a 2 decimales.
    """
    interest = calculate_simple_interest(principal, rate_percent, years)
    
    total = principal + interest
    
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_loan_details(
    principal: Union[int, float, str, Decimal],
    rate_percent: Union[int, float, str, Decimal],
    years: Union[int, float, str]
) -> dict:
    """Calcula todos los detalles del préstamo en una sola llamada.
    
    Esta función convenience retorna un diccionario con el principal,
    la tasa, el tiempo, el interés calculado y el monto total.
    
    Args:
        principal: Monto del préstamo.
        rate_percent: Tasa de interés anual en porcentaje.
        years: Tiempo en años.
    
    Returns:
        dict: Diccionario con 'principal', 'rate', 'years', 'interest' y 'total'.
    """
    principal_dec = Decimal(str(principal))
    rate_dec = Decimal(str(rate_percent))
    years_int = int(years)
    
    interest = calculate_simple_interest(principal_dec, rate_dec, years_int)
    total = calculate_total_amount(principal_dec, rate_dec, years_int)
    
    return {
        'principal': principal_dec,
        'rate': rate_dec,
        'years': years_int,
        'interest': interest,
        'total': total
    }


// === ARCHIVO: src/utils/error_messages.py ===
"""Módulo de mensajes de error predefinidos para validación y cálculos.

Contiene constantes con mensajes de error organizados por categoría
para mantener coherencia en los mensajes mostrados al usuario.
"""


class ErrorMessages:
    """Clase de contenedor para mensajes de error预definidos."""
    
    # Errores de validación de monto
    AMOUNT_INVALID_TYPE = "El monto debe ser un valor numérico válido"
    AMOUNT_NEGATIVE = "El monto del préstamo debe ser un valor positivo"
    AMOUNT_ZERO = "El monto del préstamo no puede ser cero"
    AMOUNT_TOO_LARGE = "El monto del préstamo excede el límite permitido"
    
    # Errores de validación de tasa de interés
    RATE_INVALID_TYPE = "La tasa de interés debe ser un valor numérico válido"
    RATE_NEGATIVE = "La tasa de interés no puede ser negativa"
    RATE_EXCEEDS_100 = "La tasa de interés no puede exceder el 100%"
    RATE_INVALID_FORMAT = "El formato de la tasa de interés es inválido"
    
    # Errores de validación de tiempo
    YEARS_INVALID_TYPE = "El tiempo en años debe ser un valor numérico válido"
    YEARS_NEGATIVE = "El tiempo en años debe ser positivo"
    YEARS_ZERO = "El tiempo en años no puede ser cero"
    YEARS_NOT_INTEGER = "El tiempo en años debe ser un número entero"
    YEARS_TOO_LARGE = "El tiempo en años excede el límite permitido"
    
    # Errores de cálculo
    CALCULATION_OVERFLOW = "El resultado del cálculo excede los límites numéricos"
    CALCULATION_UNDERFLOW = "El resultado del cálculo es demasiado pequeño"
    CALCULATION_PRECISION = "Error de precisión en los cálculos"
    
    # Errores generales
    INVALID_INPUT = "Los datos de entrada no son válidos"
    MISSING_INPUT = "Faltan datos requeridos para el cálculo"
    UNEXPECTED_ERROR = "Ha ocurrido un error inesperado"


def get_amount_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de monto.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'zero', 'large').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.AMOUNT_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.AMOUNT_NEGATIVE}. Valor recibido: {value}",
        "zero": f"{ErrorMessages.AMOUNT_ZERO}. Valor recibido: {value}",
        "large": f"{ErrorMessages.AMOUNT_TOO_LARGE}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.AMOUNT_INVALID_TYPE)


def get_rate_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de tasa de interés.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'exceeds').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.RATE_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.RATE_NEGATIVE}. Valor recibido: {value}",
        "exceeds": f"{ErrorMessages.RATE_EXCEEDS_100}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.RATE_INVALID_TYPE)


def get_years_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de tiempo.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'zero', 'not_integer', 'large').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.YEARS_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.YEARS_NEGATIVE}. Valor recibido: {value}",
        "zero": f"{ErrorMessages.YEARS_ZERO}. Valor recibido: {value}",
        "not_integer": f"{ErrorMessages.YEARS_NOT_INTEGER}. Valor recibido: {value}",
        "large": f"{ErrorMessages.YEARS_TOO_LARGE}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.YEARS_INVALID_TYPE)


def format_error_for_user(field_name: str, message: str) -> str:
    """Formatea un mensaje de error para mostrar al usuario final.
    
    Args:
        field_name: Nombre del campo que falló la validación.
        message: Mensaje de error técnico.
    
    Returns:
        str: Mensaje formateado para usuario.
    """
    return f"Error en '{field_name}': {message}"


// === ARCHIVO: tests/test_input_validator.py ===
import pytest
from src.validators.input_validator import validate_amount, validate_interest_rate, validate_years


class TestInputValidator:
    """Suite de pruebas para validadores de entrada."""

    def test_validate_amount_positive(self):
        """Verifica que montos positivos son aceptados."""
        result = validate_amount(1000.0)
        assert result is True

    def test_validate_amount_zero(self):
        """Verifica que el monto cero es válido."""
        result = validate_amount(0.0)
        assert result is True

    def test_validate_amount_negative(self):
        """Verifica que montos negativos son rechazados."""
        result = validate_amount(-500.0)
        assert result is False

    def test_validate_interest_rate_valid(self):
        """Verifica que tasas entre 0 y 100 son aceptadas."""
        result = validate_interest_rate(5.5)
        assert result is True

    def test_validate_interest_rate_zero(self):
        """Verifica que tasa cero es válida."""
        result = validate_interest_rate(0.0)
        assert result is True

    def test_validate_interest_rate_above_100(self):
        """Verifica que tasas mayores a 100 son rechazadas."""
        result = validate_interest_rate(150.0)
        assert result is False

    def test_validate_interest_rate_negative(self):
        """Verifica que tasas negativas son rechazadas."""
        result = validate_interest_rate(-10.0)
        assert result is False

    def test_validate_years_positive(self):
        """Verifica que años positivos son aceptados."""
        result = validate_years(5)
        assert result is True

    def test_validate_years_zero(self):
        """Verifica que cero años es válido."""
        result = validate_years(0)
        assert result is True

    def test_validate_years_negative(self):
        """Verifica que años negativos son rechazados."""
        result = validate_years(-1)
        assert result is False

    def test_validate_amount_with_string(self):
        """Verifica comportamiento con entrada no numérica."""
        with pytest.raises((TypeError, ValueError)):
            validate_amount("mil")

    def test_validate_interest_rate_with_string(self):
        """Verifica comportamiento con tasa no numérica."""
        with pytest.raises((TypeError, ValueError)):
            validate_interest_rate("cinco")

// === ARCHIVO: tests/test_interest_calculator.py ===
import pytest
from src.calculators.interest_calculator import calculate_simple_interest, calculate_total_amount


class TestInterestCalculator:
    """Suite de pruebas para cálculos de interés."""

    def test_calculate_simple_interest_basic(self):
        """Verifica cálculo básico de interés simple."""
        principal = 1000.0
        rate = 5.0
        years = 1
        result = calculate_simple_interest(principal, rate, years)
        assert result == 50.0

    def test_calculate_simple_interest_multiple_years(self):
        """Verifica cálculo con múltiples años."""
        principal = 1000.0
        rate = 10.0
        years = 3
        result = calculate_simple_interest(principal, rate, years)
        assert result == 300.0

    def test_calculate_simple_interest_zero_rate(self):
        """Verifica que tasa cero produce interés cero."""
        principal = 5000.0
        rate = 0.0
        years = 5
        result = calculate_simple_interest(principal, rate, years)
        assert result == 0.0

    def test_calculate_simple_interest_zero_years(self):
        """Verifica que cero años produce interés cero."""
        principal = 2000.0
        rate = 8.0
        years = 0
        result = calculate_simple_interest(principal, rate, years)
        assert result == 0.0

    def test_calculate_simple_interest_large_values(self):
        """Verifica cálculo con valores grandes."""
        principal = 100000.0
        rate = 12.5
        years = 10
        result = calculate_simple_interest(principal, rate, years)
        assert result == 125000.0

    def test_calculate_total_amount_basic(self):
        """Verifica cálculo del monto total."""
        principal = 1000.0
        interest = 50.0
        result = calculate_total_amount(principal, interest)
        assert result == 1050.0

    def test_calculate_total_amount_zero_interest(self):
        """Verifica monto total con interés cero."""
        principal = 1000.0
        interest = 0.0
        result = calculate_total_amount(principal, interest)
        assert result == 1000.0

    def test_calculate_total_amount_large_interest(self):
        """Verifica monto total con interés mayor al principal."""
        principal = 1000.0
        interest = 1500.0
        result = calculate_total_amount(principal, interest)
        assert result == 2500.0

    def test_calculate_simple_interest_with_fractional_rate(self):
        """Verifica cálculo con tasa fraccionaria."""
        principal = 1000.0
        rate = 4.5
        years = 2
        result = calculate_simple_interest(principal, rate, years)
        assert result == 90.0

    def test_calculate_simple_interest_with_fractional_principal(self):
        """Verifica cálculo con principal fraccionario."""
        principal = 1234.56
        rate = 10.0
        years = 1
        result = calculate_simple_interest(principal, rate, years)
        assert result == 123.456

```
