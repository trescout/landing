# Detección inalámbrica con señales WiFi

RuView es una plataforma de detección que utiliza Channel State Information (CSI) de WiFi para estudiar cambios en el entorno. Puede funcionar con hardware ESP32 o NIC de investigación, y ofrece datos simulados para evaluarla sin hardware.

- ★ 96.773
- GitHub Trending · 2026-05-30

## Actualizaciones

- **7 de octubre de 2026:** Estrellas 96,651 → 96,773, última versión v3067 (6 de octubre de 2026).
- **6 de octubre de 2026:** Estrellas 96,464 → 96,651, última versión v3060 (5 de octubre de 2026).
- **5 de octubre de 2026:** Estrellas 95,926 → 96,464, última versión v3037 (4 de octubre de 2026).
- **2 de octubre de 2026:** Estrellas 95,751 → 95,926, última versión v2975 (2 de octubre de 2026).

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

1. Prepara el entorno siguiendo la ruta de Docker o de código fuente de las guías oficiales.
2. Si no tienes hardware, empieza por la ruta de evaluación con datos simulados.
3. Ejecuta la comprobación determinista descrita en la guía de compilación mediante `./verify`.
4. Elige la ruta RSSI-only o CSI completo según tu hardware.

## Inicio seguro

El modo RSSI-only de un portátil está pensado para detectar de forma aproximada la presencia y el movimiento, y no ofrece pose. La pose y algunas capacidades de benchmark se documentan como experimentales, de primera versión o limitadas; evalúa los resultados según el modo de hardware utilizado.

## Primer prompt

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

¿Cómo puedo evaluar un escenario sencillo de detección de movimiento con datos CSI simulados de WiFi?

## Términos relacionados del glosario

- [WiFi](https://trescout.com/es/dictionary/wifi/)
- [Benchmark](https://trescout.com/es/dictionary/benchmark/)

## Enlaces

- [Repositorio en GitHub →](https://github.com/ruvnet/RuView)
- [Repositorio oficial de GitHub de RuView →](https://github.com/ruvnet/RuView)
- [Guía de usuario de RuView →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [Guía de compilación de RuView →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)
- [Leer en turco →](https://trescout.com/discover/ruview/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-05-30: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ruview/
