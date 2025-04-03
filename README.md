# 🚀 retotecnico-cobol
Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

# Introducción
Este repositorio contiene mi solución al reto técnico propuesto por Interbank. El objetivo era desarrollar una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte en la consola.

# 📌 Características
### ✅ Tecnologías usadas:
Python
### ✅ Requisitos cumplidos:
+ **1. Balance Final:** Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".
+ **2. Transacción de Mayor Monto:** Identificar el ID y el monto de la transacción con el valor más alto.
+ **3. Conteo de Transacciones:** Número total de transacciones para cada tipo ("Crédito" y "Débito").

# 🛠️ Instalación y Uso
### 1. Clona el repositorio
	git@github.com:FelipePineda15/retotecnico-cobol.git
### 2. Ejecuta la aplicación
	/usr/bin/python3 [directorio donde se clono el repositorio]
# 🔍 Enfoque y Solución:
Este código resuelve el procesamiento de transacciones bancarias (créditos/débitos) desde un archivo CSV, priorizando:

**Claridad y modularidad:**
1. Separé la lógica en funciones específicas (*read_file*, *proccess_info*, *print_message*) para facilitar el mantenimiento y la escalabilidad.
2. Cada función tiene una responsabilidad única (lectura, cálculo e impresión).

**Robustez en el manejo de datos:**
1. Limpieza automática de montos (ej. eliminar $ y convertir a float).
2. Validación implícita de tipos de transacción (Crédito/Débito) con feedback de errores.

**Eficiencia con estructuras adecuadas:**
1. Uso de una lista de diccionarios para almacenar transacciones, permitiendo acceso claro a campos (id, type, amount).
2. Cálculo del balance y transacción de mayor monto en una sola iteración (O(n)).

**Legibilidad y documentación:**
1. Docstrings explicativos en cada función.
2. Mensaje de salida formateado para fácil interpretación.

**Posibles mejoras:**
1. Implementar manejo de errores para archivos corruptos o rutas inválidas.
2. Usar bibliotecas como pandas para datasets más grandes.
## 🔍 ¿Por qué este enfoque?
El reto requería un equilibrio entre simplicidad y funcionalidad completa. Opté por Python estándar (sin dependencias externas) para garantizar portabilidad y fácil ejecución, ideal para un entorno controlado o prueba técnica.
	
