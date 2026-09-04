# Detección inalámbrica con señales WiFi

RuView es una plataforma de detección que utiliza Channel State Information (CSI) de WiFi para estudiar cambios en el entorno. Puede funcionar con hardware ESP32 o NIC de investigación, y ofrece datos simulados para evaluarla sin hardware.

- ★ 92.471
- GitHub Trending · 2026-05-30

## Instalación
**Descarga la imagen de Docker**

```
docker pull ruvnet/wifi-densepose:latest
```

**Clona el código fuente**

```
git clone https://github.com/ruvnet/RuView.git
```


## Ejecución
**Servidor de demostración sin hardware**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Comprobación determinista**

```
./verify
```


## ¿Qué hace esta herramienta?
RuView es una plataforma con licencia MIT para experimentar con detección basada en Channel State Information de WiFi. Puede instalarse con Docker o desde el código fuente y evaluarse con datos simulados sin hardware. Las capacidades dependen del modo de hardware: la detección RSSI-only en un portátil sirve para presencia y movimiento aproximados, mientras que la detección avanzada requiere hardware con CSI completo.

## ¿Para quién es?
Investigadores y desarrolladores que quieren experimentar con presencia, movimiento o cambios ambientales a partir de señales WiFi.

## Qué no esperar
Monitorización médica o expectativas de estimación de pose desde un portátil estándar en modo RSSI-only.

## Aspectos destacados
- Ofrece rutas de detección CSI con hardware ESP32 y NIC de investigación.
- Se puede evaluar con datos simulados sin hardware.
- Documenta una comprobación determinista con una señal de referencia mediante `./verify`.
- Distingue las capacidades del modo RSSI-only de un portátil de las del hardware con CSI completo.

## Primer flujo de uso
- Prepara el entorno siguiendo la ruta de Docker o de código fuente de las guías oficiales.
- Si no tienes hardware, empieza por la ruta de evaluación con datos simulados.
- Ejecuta la comprobación determinista descrita en la guía de compilación mediante `./verify`.
- Elige la ruta RSSI-only o CSI completo según tu hardware.

## Inicio seguro

## Primer prompt
¿Cómo puedo evaluar un escenario sencillo de detección de movimiento con datos CSI simulados de WiFi?

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Repositorio oficial de GitHub de RuView →
- Guía de usuario de RuView →
- Guía de compilación de RuView →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ruview/
