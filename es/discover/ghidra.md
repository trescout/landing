# Marco de análisis para ingeniería inversa de software.

Ghidra es un marco integral de ingeniería inversa de software (SRE) desarrollado por la Agencia de Seguridad Nacional (NSA) y compartido como código abierto. Plataforma desarrollada con núcleo Java y C++; Convierte archivos binarios compilados en código fuente, ofreciendo a los investigadores de seguridad descompilaciones avanzadas, análisis simbólicos y soporte para múltiples arquitecturas.

- ★ 79.733
- Java
- GitHub Trending · 2026-08-28

## Qué aporta
- Potentes descompiladores de C integrados: conversión de código de máquina e instrucciones ensambladoras en una sintaxis legible y de alto nivel similar a la de C.
- Amplia gama de procesadores y arquitecturas: soporte para x86, ARM, AArch64, MIPS, PowerPC, RISC-V, SPARC y cientos de arquitecturas de microcontroladores integrados.
- Análisis colaborativo multiusuario: anotación, denominación de funciones y control de versiones simultáneos en el mismo archivo binario con la infraestructura del servidor Ghidra.
- Automatización y análisis Headless: Escaneo automático de miles de malware en el servidor desde la línea de comando sin ingresar a la interfaz gráfica.
- Extensibilidad con Java y Python: personalice el análisis con scripts, complementos y bibliotecas de tipos de datos personalizados.

## Requisitos de instalación y sistema.
**Instalación de JDK 21 y Ghidra**

```
# macOS Homebrew ile kurulum:
brew install --cask ghidra

# Linux / Windows (Manuel arşivden başlatma):
# JDK 21 64-bit kurulu olmalıdır.
./ghidraRun          # Linux / macOS
ghidraRun.bat        # Windows
```


## Ejecución y análisis de línea de comando sin cabeza.
**Iniciando la interfaz gráfica**

```
./ghidraRun
```

**Ejecución de análisis automático sin cabeza**

```
analyzeHeadless /proje/dizini ProjeAdi -import hedef_dosya.bin -postScript GuvenlikAnalizi.py
```


## Arquitectura técnica: trineo y motor descompilador.
- Lenguaje de modelado de procesadores Sleigh: lenguaje de descripción declarativo utilizado para introducir un nuevo procesador o arquitectura de conjunto de instrucciones (ISA) en Ghidra.
- Capa de representación intermedia (IR) de código P: realización de análisis de flujo de datos y flujo de control independientes de la arquitectura traduciendo todas las instrucciones del procesador a un lenguaje intermedio común (código P).
- Motor descompilador basado en C++: motor nativo de alto rendimiento que simplifica los gráficos de flujo de control, extrae tipos de variables y reduce los bucles complejos a código C.

## Flujos de trabajo de ingeniería inversa y análisis de vulnerabilidades
- Análisis de malware (Malware Triage): apertura de ejecutables sospechosos de forma aislada y revela llamadas API ocultas, dominios C2 y claves de cifrado.
- Comparación de archivos binarios (Program Diff): Detectar la vulnerabilidad cerrada visualizando las diferencias entre dos archivos antes y después del parche de seguridad.
- Análisis de firmware: colocar volcados de memoria flash sin procesar de dispositivos IoT en el mapa de memoria y analizar las funciones del kernel y del cargador de arranque.

## Si no programa
Quiero examinar un archivo binario sospechoso usando Ghidra. ¿Puede explicar paso a paso cómo abrir un nuevo proyecto en Ghidra, importar el archivo, ejecutar el análisis automático, examinar las funciones en la ventana del descompilador y detectar funciones API sospechosas llamadas?

## Preguntas frecuentes
- ¿Cuáles son las principales diferencias entre Ghidra e IDA Pro? Si bien IDA Pro tiene tarifas comerciales y de licencia elevadas, Ghidra es completamente gratuito y de código abierto. Ghidra ofrece descompiladores integrados para todas las arquitecturas e incluye un servidor de colaboración multiusuario.
- ¿Ghidra es seguro al analizar malware? Sí, durante el análisis estático el archivo no se ejecuta, sólo se decodifica. Sin embargo, es esencial por motivos de seguridad que el análisis se realice en una máquina virtual (VM) aislada.
- ¿Cómo instalar el servidor Ghidra? Con el script svrAdmin en el directorio del servidor incluido en el paquete Ghidra, se puede abrir un servidor de equipo en la red local en unos minutos y se pueden asignar privilegios de usuario.
- ¿Se pueden ejecutar scripts de Python 3 en Ghidra? Aunque Ghidra viene con Jython (Python 2.7) de forma predeterminada, los entornos Python 3 modernos y las bibliotecas externas (NumPy, Capstone) se pueden utilizar directamente gracias al complemento PyGhidra.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ghidra/
