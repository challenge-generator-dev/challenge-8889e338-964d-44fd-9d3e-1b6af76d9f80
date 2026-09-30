# Creación de un programa simple en Python

En el contexto de una empresa fintech que desarrolla soluciones de gestión financiera, necesitas crear un programa que calcule el interés simple de un préstamo. El programa debe recibir como entrada el monto del préstamo, la tasa de interés anual y el tiempo en años. Debe calcular y mostrar el interés ganado y el monto total a pagar. Los actores involucrados son el 'usuario del sistema' y el 'motor de cálculo de intereses'. El programa debe manejar correctamente entradas inválidas, como montos negativos o tasas de interés mayores al 100%.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Programación básica con enfoque en lógica y resolución de problemas |
| **Nivel** | trainee-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 2 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de requerimientos y entrada de datos

**Objetivo:** Establecer los requerimientos del programa y asegurar que los datos de entrada sean válidos

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Define los requerimientos del programa: recibir monto del préstamo, tasa de interés anual y tiempo en años.
- Implementa la validación de datos de entrada para asegurar que el monto y la tasa de interés sean positivos y la tasa no exceda el 100%.

**Entregable:** Programa que solicita y valida la entrada de datos.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que las validaciones deben ser claras y manejar correctamente los casos de error.

</details>

### Fase 2: Cálculo del interés simple

**Objetivo:** Implementar la lógica para calcular el interés simple y el monto total a pagar

**Tiempo estimado:** 45 minutos

**Instrucciones:**

- Usa la fórmula del interés simple: Interés = Monto * Tasa * Tiempo.
- Calcula el monto total a pagar sumando el interés al monto del préstamo.

**Entregable:** Programa que calcula y muestra el interés simple y el monto total a pagar.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que la tasa de interés debe ser convertida a decimal antes de usarla en la fórmula.

</details>

### Fase 3: Mejora y pruebas del programa

**Objetivo:** Mejorar el programa para manejar más casos de error y realizar pruebas exhaustivas

**Tiempo estimado:** 45 minutos

**Instrucciones:**

- Agrega manejo de errores para casos no considerados en la fase anterior.
- Realiza pruebas con diferentes valores de entrada para asegurar que el programa funcione correctamente en todos los casos.

**Entregable:** Programa mejorado con manejo de errores adicionales y pruebas realizadas.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en posibles entradas que podrían causar errores y cómo manejarlos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es el interés simple y cómo se calcula?
- **paraQueSirve**: ¿Para qué sirve calcular el interés simple en un préstamo?
- **comoSeUsa**: ¿Cómo se usa la fórmula del interés simple en el programa?
- **erroresComunes**: ¿Qué errores comunes pueden ocurrir al calcular el interés simple y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones debes tomar al mejorar el programa para manejar más casos de error?

## Criterios de Evaluacion

- Definición clara de requerimientos y validación de datos de entrada.
- Implementación correcta de la fórmula del interés simple.
- Manejo de errores adicionales y pruebas exhaustivas del programa.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
