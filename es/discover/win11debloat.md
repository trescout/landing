# Limpie su sistema Windows de elementos innecesarios

Win11Debloat es un script de PowerShell que permite eliminar aplicaciones preinstaladas y deshabilitar datos de telemetría en los sistemas operativos Windows 10 y 11. Permite a los usuarios personalizar sus sistemas y realizar la eliminación del sistema eliminando componentes innecesarios.

- ★ 56.315
- GitHub Trending · 2026-06-16

**Nota de TreScout:** Elimina aplicaciones no deseadas que vienen con Windows y desactiva las configuraciones que recopilan datos en segundo plano. Lea lo que hace antes de ejecutarlo: no es fácil recuperar algunas piezas eliminadas. No lo use en una computadora personal, en un dispositivo de la empresa o en una computadora que comparta con otra persona.

## Actualizaciones

- **27 de agosto de 2026:** Estrellas 54,506 → 56,315, última versión 2026.08.24 (24 de agosto de 2026).
- **2 de agosto de 2026:** Estrellas 48,210 → 54,506, última versión 2026.07.11 (11 de julio de 2026).

*Kaynak: github.com/Raphire/Win11Debloat · MIT*

## Qué aporta

- Elimina rápidamente aplicaciones preinstaladas innecesarias.
- Desactiva la telemetría y los datos de seguimiento.
- Desactiva las funciones y los anuncios basados ​​en IA.

## Instalación

**Descargar archivo de GitHub**

```
Invoke-WebRequest -Uri https://github.com/Raphire/Win11Debloat/archive/refs/heads/master.zip -OutFile Win11Debloat.zip
```

**Abrir archivo**

```
Expand-Archive -Path .\Win11Debloat.zip -DestinationPath .\Win11Debloat
```

## Ejecución

**Ejecutar script revisándolo**

```
Set-Location .\Win11Debloat\Win11Debloat-master
.\Win11Debloat.ps1
```

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero desinstalar aplicaciones innecesarias en mi sistema operativo Windows 11, desactivar los datos de telemetría y desactivar funciones como Copilot con tecnología de IA. ¿Cómo puedo hacer que mi sistema sea más liviano y centrado en la privacidad usando la herramienta Win11Debloat? Explique paso a paso a qué debo prestar atención para mantener la estabilidad del sistema cuando uso esta herramienta y cómo puedo personalizarla de forma segura.

## Términos relacionados del glosario

- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Es para usuarios que utilizan el sistema operativo Windows 10 u 11 y desean limpiar su sistema de componentes innecesarios y controlar su configuración de privacidad.
- **Licencia:** MIT

## Enlaces

- [Repositorio en GitHub →](https://github.com/Raphire/Win11Debloat)
- [Leer en turco →](https://trescout.com/discover/win11debloat/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-06-16: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/win11debloat/
