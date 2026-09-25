# Escáner de seguridad para contenedores y nube

Trivy es una herramienta de escaneo de seguridad integral y ultrarrápida que detecta vulnerabilidades (CVEs), configuraciones erróneas y secretos expuestos en contenedores, clústeres de Kubernetes y repositorios. Con soporte nativo para SBOM, automatiza la seguridad DevSecOps de extremo a extremo.

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Qué aporta
- Análisis multiobjetivo unificado: Inspecciona imágenes de contenedores (Docker, OCI), sistemas de archivos, repositorios Git remotos y clústeres de Kubernetes.
- Cero sobrecarga de infraestructura: No requiere bases de datos externas ni demonios persistentes en segundo plano; funciona como un único binario autónomo.
- Detección de secretos y datos confidenciales: Encuentra claves API, contraseñas y certificados privados incrustados por error en el código o en las capas de imagen.
- Auditoría de Infraestructura como Código (IaC): Valida plantillas Terraform, Dockerfile y manifiestos Kubernetes YAML antes del despliegue en producción.
- SBOM y cumplimiento de licencias: Genera listas de materiales de software (SBOM) bajo estándares CycloneDX y SPDX para cumplir normativas de cadena de suministro.

## Instalación

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Uso básico

**Escanear imagen de contenedor**

```
trivy image nombre-imagen:tag
```

**Escanear código local y secretos**

```
trivy fs --scanners vuln,secret,misconfig .
```

**Generar SBOM en formato CycloneDX**

```
trivy image --format cyclonedx --output sbom.json nombre-imagen:tag
```

## Arquitectura técnica y funcionamiento interno

Desarrollado por Aqua Security y la comunidad open source, Trivy incorpora un motor de alto rendimiento adaptado a flujos DevSecOps:
- Base de datos local (Trivy DB): Sincroniza automáticamente una base de vulnerabilidades compacta (NVD, GitHub Advisory, Red Hat, Debian) para análisis sin conexión.
- Análisis estático de capas: Desempaqueta las capas OCI sin ejecutar el contenedor ni requerir privilegios del demonio Docker.
- Motor IaC con políticas Rego: Evalúa plantillas de infraestructura con reglas Open Policy Agent (OPA) para bloquear puertos inseguros y ejecuciones root.
- Mapeo exhaustivo de dependencias: Examina archivos de bloqueo (package-lock.json, poetry.lock, Cargo.lock) para destapar riesgos transitivos.

## Integración DevSecOps y pipelines de CI/CD

Trivy actúa como una barrera de calidad (quality gate) para impedir que el código con brechas de seguridad alcance los entornos de producción:

**Detener la compilación ante vulnerabilidades críticas o altas**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH nombre-imagen:tag
```
- Detección temprana (Shift-left): Los desarrolladores identifican problemas en librerías de terceros en su máquina antes de subir cambios.
- Informes automáticos en SARIF: Carga los resultados a GitHub Code Scanning o GitLab Security para un seguimiento centralizado de riesgos.
- Monitorización de clústeres (Trivy Operator): Supervisa continuamente cargas de trabajo en Kubernetes para alertar sobre vulnerabilidades de día cero.

## Si no programas
🤖 Si no programas
Quiero configurar un flujo de trabajo de GitHub Actions que analice mi imagen Docker y código con Trivy en cada push y PR. ¿Podrías crear un archivo .github/workflows/trivy.yml completo que falle (exit-code 1) solo con vulnerabilidades CRITICAL y HIGH, suba los resultados en SARIF a la pestaña de Seguridad de GitHub y genere un artefacto SBOM en formato CycloneDX?

- **Para quién:** Ingenieros DevOps, especialistas en seguridad y desarrolladores que buscan automatizar auditorías de vulnerabilidades y crear SBOM.
- **Licencia:** Apache-2.0 (Licencia de código abierto permisiva)
- **Desarrollador:** Aqua Security y comunidad de código abierto
- **Formatos de salida:** Tabla, JSON, SARIF, CycloneDX, SPDX, Plantilla

## Preguntas frecuentes
- ¿Puede Trivy escanear imágenes sin el demonio de Docker? Sí. Trivy puede descargar e inspeccionar imágenes directamente desde registros remotos (Docker Hub, GitHub Container Registry) o leer archivos tar locales sin Docker activo.
- ¿Funciona en redes aisladas (air-gapped)? Sí. La base de datos de Trivy se puede descargar previamente y copiar a entornos cerrados para ejecutar escaneos sin acceso a internet.
- ¿Qué es un SBOM y por qué utilizar Trivy? Un SBOM es el inventario digital de librerías y licencias de una aplicación. Trivy genera archivos CycloneDX y SPDX estandarizados para código e imágenes.
- ¿Qué tan rápido es un escaneo habitual? Al realizar las consultas contra una base de datos local preindexada sin peticiones de red intermedias, los escaneos suelen completarse en pocos segundos.

## Enlaces
- [GitHub →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

## Términos relacionados del glosario
Container CI-CD Vulnerability Scanning Cloud Native

---
Source: TreScout Discover · https://trescout.com/es/discover/trivy/
