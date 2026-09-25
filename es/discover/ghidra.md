# Suite de ingeniería inversa y análisis de software

Ghidra es una completa suite de ingeniería inversa de software (SRE) de código abierto desarrollada y publicada por la National Security Agency (NSA). Construida en Java con un descompilador en C++ de alto rendimiento, decompila binarios a código fuente comprensible y ofrece análisis simbólico avanzado en múltiples arquitecturas.

- ★ 78.142
- Java
- GitHub Trending · 2026-08-28

## Actualizaciones
- 17 de septiembre de 2026: Estrellas 78.142, última versión Ghidra_12.1.3_build (soporte para Java 21, mejoras en descompilador para RISC-V y ARM64).

## Qué te aporta
- Descompilador de C integrado y potente: Convierte instrucciones en código máquina y ensamblador directamente en pseudocódigo C estructurado.
- Amplio catálogo de arquitecturas: Soporte para x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC y cientos de microcontroladores.
- Análisis colaborativo multiusuario: Varios analistas pueden trabajar simultáneamente sobre el mismo binario mediante Ghidra Server.
- Análisis desatendido (Headless): Automatiza el análisis masivo de malware y auditorías de seguridad desde la consola sin abrir la interfaz gráfica.
- Extensibilidad con Java y Python: Programa scripts personalizados, desempacadores automáticos y parseadores de estructuras de datos.

## Instalación y requisitos de sistema

**Instalación de JDK 21 y Ghidra**

```
# En macOS con Homebrew:
brew install --cask ghidra

# Linux / Windows (Inicio manual desde el archivo descargado):
# Requiere tener instalado JDK 21 de 64 bits.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```

## Ejecución y análisis headless por línea de comandos

**Iniciar la interfaz gráfica**

```
./ghidraRun
```

**Ejecutar análisis desatendido sin GUI**

```
analyzeHeadless /ruta/proyecto NombreProyecto -import ejecutable.bin -postScript Auditoria.py
```

## Arquitectura técnica: Sleigh y motor de descompilación

La sólida base arquitectónica que distingue a Ghidra se compone de:
- Lenguaje de especificación Sleigh: Lenguaje declarativo orientado a describir conjuntos de instrucciones y registros de nuevas CPUs.
- Representación intermedia P-Code: Normaliza todas las instrucciones a un formato común para analizar flujos de datos sin importar la arquitectura.
- Motor descompilador nativo en C++: Reduce instrucciones redundantes, estructura bucles de control y reconstruye tipos de variables velozmente.

## Flujos de trabajo en ingeniería inversa y análisis de vulnerabilidades

Ghidra actúa como estación central en tareas de ciberseguridad defensiva y ofensiva:
- Análisis y clasificación de malware: Inspecciona ficheros sospechosos para descubrir cadenas ofuscadas, dominios C2 y llamadas al sistema.
- Comparación binaria (Program Diff): Contrasta dos versiones de un ejecutable para entender parches de seguridad y vectores de explotación.
- Auditoría de firmwares embebidos: Reconstruye volcados de memoria flash de dispositivos IoT para analizar bootloaders y rutinas del núcleo.

## Si no programas
🤖 Si no programas
Quiero examinar un archivo ejecutable sospechoso usando Ghidra. ¿Podrías explicarme paso a paso cómo crear un nuevo proyecto, importar el binario, ejecutar el Auto Analysis, navegar por la ventana del Decompiler e identificar llamadas a funciones sensibles del sistema?

- **Para quién:** Analistas de malware, investigadores de vulnerabilidades, especialistas en ingeniería inversa y desarrolladores de firmware.
- **Licencia:** Apache-2.0 (Licencia permisiva de código abierto)
- **Desarrollador:** National Security Agency (NSA) y comunidad de código abierto
- **Requisitos:** Java Development Kit (JDK) 21 64-bit

## Preguntas frecuentes
- ¿Qué diferencias principales hay entre Ghidra e IDA Pro? IDA Pro es un software comercial con licencias de alto coste por arquitectura, mientras que Ghidra es completamente gratuito, de código abierto, incluye descompilador para todas las CPUs y cuenta con servidor colaborativo integrado.
- ¿Es seguro analizar código malicioso con Ghidra? Sí, el análisis estático se limita a desensamblar y traducir el código sin ejecutar el archivo binario. De todos modos, se recomienda trabajar siempre dentro de una máquina virtual aislada.
- ¿Cómo se configura Ghidra Server? Mediante el script svrAdmin incluido en la carpeta server, se puede desplegar un servidor de trabajo en equipo en la red local en cuestión de minutos.
- ¿Se pueden ejecutar scripts en Python 3 dentro de Ghidra? Aunque Ghidra integra Jython (Python 2.7) de forma predeterminada, con el plugin PyGhidra se pueden utilizar scripts en Python 3 nativo junto a bibliotecas como NumPy o Capstone.

## Enlaces
- [GitHub →](https://github.com/NationalSecurityAgency/ghidra)

## Términos relacionados del glosario
Binary Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/es/discover/ghidra/
