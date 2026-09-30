# Radar de matriz en fase de código abierto

PLFM RADAR es un sistema de radar de matriz en fase de código abierto que funciona a 10,5 GHz (banda X) con dirección electrónica del haz y capacidades de procesamiento de señales digitales basadas en FPGA. Detecta y rastrea objetivos aéreos y terrestres con alta precisión sin utilizar piezas mecánicas móviles.

- ★ 25.440
- C++
- GitHub Trending · 2026-08-18

## Qué aporta
- Dirección electrónica del haz: escanea un sector de 90 grados con desfasadores en milisegundos sin necesidad de un motor mecánico o una antena giratoria.
- Modo de funcionamiento de doble alcance: capacidad de operación de 3 km en corto alcance (detección de UAV/Drones), 20 km en largo alcance (vigilancia perimetral y seguimiento de aeronaves).
- Procesamiento de señales en tiempo real basado en FPGA: Procesamiento de hardware de ecos de radar sin procesar en FPGA con algoritmos FFT y CFAR de alta velocidad.
- Hardware accesible de bajo costo: Reducir el costo de los radares comerciales y militares de cientos de miles de dólares a menos de mil dólares con diseños de PCB de código abierto.
- Integración de Python y SDR: monitoreo en vivo de datos de radar digital a través de hardware SDR de código abierto y una interfaz Python.

## Componentes de hardware y arquitectura de radar.
- Conjunto de antenas microstrip de banda X de 10,5 GHz: elementos de antena multiparche diseñados en capas Rogers/FR4 de baja pérdida.
- Desfasadores controlados numéricamente: circuitos integrados de RF que dirigen el haz en el espacio retrasando la fase de la señal de cada elemento de la antena con una precisión de 5,6 grados.
- Sintetizador de frecuencia FMCW: Oscilador local de alta estabilidad (VCO/PLL) que genera onda continua con modulación de frecuencia lineal.

## Software de procesamiento y control de señales.
- Range-Doppler FFT (2D FFT): Cálculo simultáneo de la distancia del objetivo y la velocidad radial aplicando primero el rango y luego Doppler FFT a la señal entrante.
- Detector CFAR (tasa de falsas alarmas constantes): separa objetivos en movimiento reales del ruido de fondo y ecos del suelo (desorden) con umbralización dinámica.
- Pantalla Python GUI y PPI: visualización de seguimientos de objetivos en un mapa en vivo en una pantalla de radar circular tradicional (PPI).

## Principio de funcionamiento técnico: FMCW y Phased Array
- Medición de distancia a partir de la diferencia de frecuencia: la frecuencia de batido se obtiene mezclando la señal de chirrido enviada con la señal que regresa del objetivo. Esta frecuencia es directamente proporcional a la distancia.
- Enfoque del haz con interferencia constructiva: al dar un cierto retraso de fase a cada elemento de antena del conjunto, la señal recibe interferencia constructiva en la dirección deseada e interferencia destructiva en otras direcciones.

## Escenarios de uso y pruebas de campo.
- Defensa con drones y vehículos aéreos no tripulados de baja altitud: detección de pequeños vehículos aéreos no tripulados en condiciones de niebla o nocturnas donde las cámaras ópticas son inadecuadas.
- Seguridad del perímetro de instalaciones críticas: Monitoreo de aproximaciones de personas o vehículos no autorizados dentro de un radio de 3 km en aeropuertos, centros de datos y sitios industriales.
- Investigación meteorológica y atmosférica: análisis de los movimientos de las nubes y la intensidad de las precipitaciones a escala local mediante métodos micro-Doppler.

## Si no programa
Me gustaría revisar los esquemas de hardware de matriz en fase de 10,5 GHz y los bloques de procesamiento de señales FPGA del proyecto PLFM RADAR. ¿Puede crear un script de simulación en Python que describa la generación de señales de chirrido FMCW, el cálculo de FFT 2D Range-Doppler y la transferencia de datos a una pantalla de radar PPI basada en Python? ¿Puedes mostrar paso a paso el algoritmo de detección de distancia y velocidad para un objetivo artificial?

## Preguntas frecuentes
- ¿Es posible producir el sistema en casa o en el laboratorio? Sí. Todos los esquemas de PCB, archivos de producción Gerber y códigos FPGA Verilog/VHDL del proyecto están disponibles como código abierto en el repositorio de GitHub. Las placas se pueden solicitar a fabricantes de PCB estándar y soldarse en un entorno de laboratorio.
- ¿Cuál es la ventaja de la dirección electrónica del haz sobre los radares mecánicos? Mientras que los radares mecánicos giran entre 1 y 2 revoluciones por segundo, los radares en fase pueden cambiar la dirección del haz en microsegundos. No hay piezas mecánicas desgastadas y puede fijar múltiples objetivos al instante.
- ¿Se requiere un permiso especial de radiofrecuencia para operar? La banda de 10,5 GHz está sujeta a asignaciones de frecuencias para radioaficionados o industriales/científicas (ISM) en muchos países. Aunque se permiten pruebas en laboratorio con potencias de salida bajas, se deben observar las regulaciones locales para transmisiones de largo alcance en exteriores.
- ¿Con qué placas de desarrollo FPGA es compatible? La serie Xilinx Zynq-7000 o las modernas tarjetas AMD UltraScale+ RFSoC son directamente compatibles; Las interfaces ADC/DAC de alta velocidad se conectan a través del conector FMC.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/plfm-radar/
