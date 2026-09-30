# Escáner de seguridad de contenedores y nube

Trivy es una herramienta integral de escaneo de seguridad que detecta vulnerabilidades, configuraciones incorrectas y secretos en contenedores, clústeres de Kubernetes, repositorios de código e infraestructuras de nube en segundos. Automatiza los procesos de DevSecOps de un extremo a otro con soporte de lista de materiales de software (SBOM).

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Qué aporta
- Escaneo de objetivos de múltiples capas: inspecciona imágenes de contenedores (Docker, OCI), sistemas de archivos locales, repositorios Git remotos, discos de máquinas virtuales y clústeres de Kubernetes en vivo con una sola herramienta.
- Cero gastos generales de infraestructura adicional: no es necesario un servidor de base de datos externo ni agentes pesados ​​que se ejecuten constantemente; Ofrece análisis en segundos como un único binario ejecutable.
- Captura de secretos y datos confidenciales: detecta claves API, contraseñas y certificados privados incrustados accidentalmente en el código fuente o capas de imágenes con su motor heurístico.
- Auditoría de infraestructura como código (IaC): detecta configuraciones erróneas de seguridad en archivos Terraform, Dockerfile, Kubernetes YAML y CloudFormation antes de que pasen a producción.
- Cumplimiento de SBOM y licencia de código abierto: cumple con la seguridad de la cadena de suministro de software con las regulaciones legales al producir una lista de materiales de software en los estándares CycloneDX y SPDX.

## Instalación
**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```


## Ejecución
**Escanear imagen de contenedor**

```
trivy image imaj-adi:etiket
```


## Arquitectura técnica y principio de funcionamiento
- Trivy DB y caché local: NVD descarga automáticamente un caché de base de datos liviano que contiene boletines de seguridad de GitHub Advisory Database, Red Hat, Debian, Ubuntu y Alpine. Dado que los análisis se realizan a través de este caché local, se ejecuta a la velocidad del rayo incluso en entornos con restricciones de red.
- Análisis de capas estáticas: analiza directamente las capas OCI sin ejecutar imágenes de contenedores ni necesitar un demonio Docker. Este enfoque no compromete la seguridad del sistema durante el proceso de escaneo.
- Motor IaC y políticas Rego: controla las plantillas de infraestructura con reglas compatibles con Open Policy Agent (OPA). Los puertos abiertos inseguros o los servicios que se ejecutan con privilegios de root se informan de inmediato.
- Estandarización de SBOM: el administrador de paquetes escanea los archivos de bloqueo (package-lock.json, poesía.lock, Cargo.lock, etc.) y crea un mapa de dependencia completo de su aplicación.

## Integración de canalización de DevSecOps y CI/CD
- Comentarios de la etapa inicial: los desarrolladores ven instantáneamente vulnerabilidades en las bibliotecas de código abierto al ejecutar Trivy en su entorno local antes de enviar su código al repositorio remoto.
- Informes SARIF automáticos: los resultados SARIF producidos se transfieren a los paneles de escaneo de código de GitHub o de seguridad de GitLab, lo que permite a los equipos realizar un seguimiento central de vulnerabilidades.
- Monitoreo de clústeres en vivo (Trivy Operador): monitorea constantemente las cargas de trabajo que se ejecutan en el entorno de Kubernetes e informa instantáneamente las vulnerabilidades de día cero (día 0) recién descubiertas.

## Si no programa
Quiero configurar un flujo de trabajo de seguridad en GitHub Actions que escanee mi imagen de Docker y mis códigos fuente con Trivy en cada solicitud de inserción y extracción de código (PR). ¿Puede crear un archivo .github/workflows/trivy.yml completo que detenga la compilación solo en vulnerabilidades CRÍTICAS y de ALTO nivel (código de salida 1), cargue los hallazgos en el panel de seguridad de GitHub en formato SARIF y cree un archivo SBOM en formato CycloneDX?

## Preguntas frecuentes
- ¿Trivy Docker puede escanear imágenes de contenedores sin un demonio? Sí. Trivy puede descargar y escanear imágenes directamente desde repositorios de imágenes remotos (Docker Hub, GitHub Container Registry, AWS ECR, etc.) o archivos tar locales sin la necesidad de un cliente o demonio Docker.
- ¿Funciona en entornos aislados sin conexión a Internet? Sí. La base de datos Trivy (trivy-db) se puede descargar con anticipación y trasladar a un entorno de red cerrado. Trivy puede escanear el caché de la base de datos local sin conectarse.
- ¿Qué es SBOM y por qué se prefiere Trivy en este campo? SBOM (Lista de materiales de software) es una lista de contenido digital que documenta todas las bibliotecas, versiones y licencias de código abierto incluidas en su software. Trivy es una de las pocas herramientas estándar que puede producir SBOM tanto a nivel de imagen como a nivel de código fuente.
- ¿Cómo excluir falsos positivos o riesgos aceptados? Puede enumerar los códigos CVE que desea ignorar línea por línea agregando un archivo .trivyignore al directorio raíz del proyecto. De esta manera, se evitan interrupciones innecesarias de compilación en las canalizaciones de CI/CD.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/trivy/
