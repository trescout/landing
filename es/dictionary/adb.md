# ¿Qué es ADB?

> Android Debug Bridge

ADB (Android Debug Bridge, puente de depuración de Android) es una herramienta que permite la comunicación de comandos y depuración entre un ordenador y un dispositivo Android.

## Definición y origen de la palabra
"Debug" depuración, "bridge" significa puente. ADB establece la comunicación entre el cliente en el ordenador y el demonio adb en el dispositivo; se utiliza para la instalación de aplicaciones, la recopilación de registros, la depuración y operaciones limitadas de gestión de dispositivos. Es parte del paquete Android SDK Platform-Tools.

## ¿Cómo saberlo y utilizarlo en la vida diaria?
Desarrollo: Instalación y registro de aplicaciones.Prueba: Pruebas en múltiples dispositivos.Personalización: Configuración avanzada.

## Profundidad técnica y arquitectura
Estructura triple:

## Cosas frecuentemente mezcladas
Se confunde con la transferencia de archivos. Aquello solo copia, ADB interviene en el sistema. La diferencia de privilegios es grande.

## Uso en diferentes disciplinas
Cable: La línea que transporta la señal.Intérprete: El lenguaje de ambas partes.Control: Gestión remota.

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
- [CLI](/es/dictionary/cli/)
- [SDK](/es/dictionary/sdk/)
- [Emulator](/es/dictionary/emulator/)

## Herramientas relacionadas
- [Universal Android Debloater Next Generation](/es/discover/universal-android-debloater-next-generation/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/adb/
