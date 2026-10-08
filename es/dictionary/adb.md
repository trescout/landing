# ¿Qué es ADB?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

> Android Debug Bridge

ADB (Android Debug Bridge, puente de depuración de Android) es una herramienta que permite la comunicación de comandos y depuración entre un ordenador y un dispositivo Android.

## Definición y origen de la palabra

"Debug" depuración, "bridge" significa puente. ADB establece la comunicación entre el cliente en el ordenador y el demonio adb en el dispositivo; se utiliza para la instalación de aplicaciones, la recopilación de registros, la depuración y operaciones limitadas de gestión de dispositivos. Es parte del paquete Android SDK Platform-Tools.

***Analogía:** Si considera la computadora como el centro de control y el dispositivo como la nave espacial, ADB es el cable de señal entre ellos.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Desarrollo:** Instalación y registro de aplicaciones.
**Prueba:** Pruebas en múltiples dispositivos.
**Personalización:** Configuración avanzada.

## Profundidad técnica y arquitectura

Estructura triple:

**Cliente:** El comando en la computadora.
**Presentador:** El administrador que se ejecuta en segundo plano.
**Daemon:** El receptor en el dispositivo.

Flujo:

```
adb devices
adb install uygulama.apk
```

El primero enumera los dispositivos conectados, el segundo instala el paquete de la aplicación. La depuración USB debe estar habilitada en el dispositivo. Dado que los comandos incorrectos pueden provocar la pérdida de datos, es necesario verificar el dispositivo de destino y el comando antes de ejecutarlos.

## Cosas frecuentemente mezcladas

Se confunde con la transferencia de archivos. Aquello solo copia, ADB interviene en el sistema. La diferencia de privilegios es grande.

## Uso en diferentes disciplinas

**Cable:** La línea que transporta la señal.
**Intérprete:** El lenguaje de ambas partes.
**Control:** Gestión remota.

## Preguntas frecuentes

**¿Todos pueden usarlo?**

Los comandos básicos se pueden aprender; sin embargo, especialmente adb shell y las operaciones de borrado requieren conocimientos técnicos. Es necesario verificar el efecto del comando antes de ejecutarlo.

**¿Se puede hacer de forma inalámbrica?**

Sí. En las versiones de Android compatibles, se puede establecer una conexión a través de Wi-Fi después de emparejarlo con el dispositivo. La estabilidad y la velocidad dependen de la calidad de la red local.

**¿Es seguro?**

Si usted tiene el dispositivo, sí. No se otorga aprobación en un dispositivo conectado a una computadora desconocida.

**¿Cuál es la diferencia con Fastboot?**

ADB se comunica con el sistema operativo mientras Android está en ejecución. Fastboot, por otro lado, se utiliza para operaciones de imagen de partición o firmware mientras el dispositivo está en modo bootloader; los comandos compatibles y el proceso de desbloqueo varían según el dispositivo.

## Términos relacionados

- [CLI](https://trescout.com/es/dictionary/cli/)
- [SDK](https://trescout.com/es/dictionary/sdk/)
- [Emulator](https://trescout.com/es/dictionary/emulator/)

## Herramientas relacionadas

- [Universal Android Debloater Next Generation](https://trescout.com/es/discover/universal-android-debloater-next-generation/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/adb/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/adb/
