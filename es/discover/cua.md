# Control informático para agentes de inteligencia artificial.

CUA proporciona una infraestructura de código abierto para agentes de inteligencia artificial con capacidad informática. Reúne sandbox, kit de desarrollo de software (SDK) y herramientas de referencia bajo un mismo techo con el fin de capacitar y evaluar agentes que puedan controlar los sistemas operativos de escritorio.

- ★ 21.225
- HTML
- GitHub Trending · 2026-06-16

## Qué aporta
- Controlar las aplicaciones de escritorio en segundo plano
- Sandboxes aislados para diferentes sistemas operativos
- Herramientas de evaluación comparativa para medir el desempeño de los agentes

## Instalación
**Instalación de controladores (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Instalación del SDK de espacio aislado**

```
pip install cua
```


## Ejecución
**Inicio de la máquina virtual macOS**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```


## Si no programa
Quiero desarrollar un agente de uso de computadora utilizando la infraestructura CUA. Ayúdenme a configurar la estructura básica de Python que permitirá a mi agente interactuar con aplicaciones de escritorio en segundo plano, hacer clic con el mouse y enviar entradas de teclado. Cree un boceto de código de muestra que ejecute comandos y tome capturas de pantalla en un entorno Linux utilizando el SDK de CUA Sandbox.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/cua/
