# Sistema radar phased array de código abierto

PLFM RADAR es un sistema radar phased array de código abierto que opera en 10.5 GHz (banda X), con direccionamiento electrónico del haz (electronic beam steering) y procesamiento digital de señales sobre FPGA. Detecta y monitoriza objetivos aéreos y terrestres sin mecanismos giratorios.

- ★ 24.168
- C++
- GitHub Trending · 2026-08-18

## Actualizaciones
- 18 de agosto de 2026: Estrellas 24.168, versión estable v2.0.2-p0-audit (filtrado de señales en FPGA y calibración de alcance).

## Qué te aporta
- Direccionamiento electrónico del haz: Barre un sector de 90 grados en milisegundos mediante desfasadores digitales sin piezas móviles ni desgaste.
- Dos modos de alcance operativo: Modo táctico de 3 km para detección de drones y modo de largo alcance de 20 km para vigilancia perimétrica.
- Procesamiento en tiempo real sobre FPGA: Aceleración por hardware de algoritmos FFT y detección CFAR directamente en el silicio.
- Hardware asequible de bajo coste: Reduce los cientos de miles de dólares de los radares militares comerciales a menos de mil dólares.
- Integración con Python y SDR: Visualiza trayectorias de blancos en tiempo real mediante receptores SDR y pantallas PPI en Python.

## Componentes de hardware y arquitectura del radar

La arquitectura de PLFM RADAR comprende front-end de RF, conjunto de antenas planas y capa de procesamiento digital:
- Matriz de antenas patch microstrip en 10.5 GHz: Elementos de antena diseñados sobre sustrato Rogers/FR4 de bajas pérdidas para alta frecuencia.
- Desfasadores controlados digitalmente: Retardan la fase de cada elemento en pasos de 5.6 grados para apuntar el haz en el espacio.
- Sintetizador de frecuencia FMCW: Oscilador local (VCO/PLL) de alta estabilidad que genera ondas continuas moduladas en frecuencia.

## Procesamiento de señal y software de control

Los ecos captados se procesan a nivel de hardware para obtener distancia, velocidad radial y acimut:
- 2D FFT Distancia-Doppler: Aplica transformadas de Fourier bidimensionales para discernir simultáneamente la distancia y la velocidad.
- Detector CFAR (Tasa Constante de Falsas Alarmas): Ajusta dinámicamente el umbral para discriminar ecos reales frente al ruido de fondo.
- Interfaz en Python y pantalla PPI: Proyecta los blancos en tiempo real sobre una pantalla de radar clásica (PPI) superpuesta a mapas.

## Principio técnico de operación: FMCW y phased array

PLFM RADAR utiliza la tecnología de onda continua modulada en frecuencia (FMCW) en lugar de pulsos convencionales de alta potencia:
- Medición de distancia por frecuencia de batido: Mezclar la señal chirp emitida con el eco recibido genera una frecuencia intermedia proporcional a la distancia.
- Conformación de haz por interferencia constructiva: Regular la fase relativa en cada antena focaliza la energía electromagnética en la dirección elegida.

## Casos de uso y pruebas de campo

El diseño de phased array abierto hace viable un gran espectro de aplicaciones:
- Defensa antidron a baja cota: Detecta pequeños drones bajo niebla o de noche cuando las cámaras térmicas u ópticas no alcanzan.
- Seguridad perimetral en puntos críticos: Monitoriza accesos no autorizados en un radio de 3 km alrededor de aeropuertos y centros de datos.
- Investigación meteorológica: Mide rachas de viento locales y reflectividad de precipitaciones mediante análisis micro-Doppler.

## Si no programas
🤖 Si no programas
Quiero explorar los esquemas de hardware a 10.5 GHz y el procesado DSP en FPGA del proyecto PLFM RADAR. ¿Podrías escribir un script de simulación en Python que genere una señal chirp FMCW, calcule la 2D FFT Distancia-Doppler y extraiga la distancia y velocidad de un dron simulado?

- **Para quién:** Investigadores de radar, ingenieros de defensa, desarrolladores de sistemas antidron y aficionados a RF/SDR.
- **Licencia:** Licencia de hardware y software de código abierto
- **Banda de frecuencia:** 10.5 GHz (Banda X) FMCW
- **Alcance operativo:** 3 km (táctico antidron) a 20 km (vigilancia de área extensa)

## Preguntas frecuentes
- ¿Es posible montar este sistema en un laboratorio casero? Sí. Todos los esquemas, ficheros Gerber de fabricación y código Verilog/VHDL para FPGA están disponibles en GitHub para encargar y soldar en laboratorio.
- ¿Qué ventaja ofrece el phased array frente a una antena giratoria? El haz se orienta en microsegundos de forma electrónica, lo que elimina el desgaste mecánico y permite el seguimiento continuo e intercalado de múltiples blancos.
- ¿Se requiere autorización de radiofrecuencia para emitir? La banda de 10.5 GHz suele tener asignaciones de radioaficionados o ISM. En laboratorio a baja potencia no suele haber restricciones, pero las pruebas al aire libre deben respetar las leyes locales.
- ¿Qué placas FPGA son compatibles? Las plataformas Xilinx Zynq-7000 y AMD UltraScale+ RFSoC se conectan de manera directa mediante conectores FMC a las tarjetas ADC/DAC.

## Enlaces
- [GitHub →](https://github.com/NawfalMotii79/PLFM_RADAR)

## Términos relacionados del glosario
Edge Computing Open Source Local Offline

---
Source: TreScout Discover · https://trescout.com/es/discover/plfm-radar/
