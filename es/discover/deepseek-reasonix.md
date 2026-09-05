# Agente de codificación AI para terminal

DeepSeek-Reasonix es un agente de codificación de IA que se ejecuta en el terminal y se basa en modelos de DeepSeek. Esta herramienta, que se centra en la estabilidad de la caché de prefijos, garantiza que los desarrolladores reciban soporte de codificación ininterrumpido durante largas sesiones.

- ★ 35.396
- Go
- GitHub Trending · 2026-08-03

## Qué aporta
- Proporciona soporte de codificación ininterrumpida a largo plazo con modelos DeepSeek.
- Ofrece gestión de sesiones de bajo coste con su función de almacenamiento en caché de prefijos.
- Proporciona un uso flexible a través del terminal con soporte de complemento configurable.

## Instalación
**Instalación mediante NPM o Homebrew**

```
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

**Compilando desde el código fuente**

```
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```


## Ejecución
**Configuración e inicialización**

```
reasonix setup                      # configure a provider and model
reasonix                            # start an interactive session
reasonix run "implement the TODOs in main.go"
```


## Si no programa
Mientras trabajo con este agente de codificación de inteligencia artificial que se ejecuta en la terminal, desarrollo sugerencias de código teniendo en cuenta la estructura actual y los objetivos de mi proyecto. Concéntrese en producir respuestas consistentes y de bajo costo durante nuestras largas sesiones utilizando la estabilidad de la caché de prefijo. Al escribir o depurar código, proporcione soluciones modulares y limpias que se ajusten a las necesidades del proyecto.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/deepseek-reasonix/
