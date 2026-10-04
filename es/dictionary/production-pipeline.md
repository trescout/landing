# ¿Qué es Production Pipeline?

El pipeline de producción (production pipeline) es una cadena de procesos de ingeniería integrados que permite que el código fuente escrito por los desarrolladores de software sea compilado, probado, sometido a escaneos de seguridad, empaquetado y desplegado automáticamente en el entorno de producción con cero tiempo de inactividad.

## Origen conceptual, etimología y filosofía de la línea de producción
La palabra "pipeline" se toma prestada de las tuberías de transporte de petróleo y agua, y "production" de las líneas de montaje (assembly line) de las fábricas industriales, para aplicarlas a la ingeniería de software. Al igual que la revolución que Henry Ford creó en la industria automotriz con la línea de producción en serie a principios del siglo XX, el pipeline de producción es el estándar de producción industrial moderno que pone fin a los procesos de despliegue manuales, propensos a errores y ambiguos en el sector del software.

## 5 estaciones críticas de una línea de producción
Un pipeline de producción corporativo completo consta de los siguientes pasos:

## Distinciones sectoriales: Tubería de producción (Production Pipeline) vs. Tubería de datos (Data Pipeline) vs. Tubería de efectos visuales (VFX Pipeline)
La palabra "Pipeline" tiene diferentes significados en distintas disciplinas técnicas:

## Métricas DORA y productividad de ingeniería
La madurez del pipeline de producción de una organización se mide con las cuatro métricas de oro determinadas en la investigación DORA (DevOps Research and Assessment) de Google:

## Preguntas frecuentes
**¿Qué significa pipeline de producción y cuál es su objetivo principal?**
Significa tubería o flujo de producción de software. Su objetivo es que el código fuente desarrollado sea probado y compilado automáticamente, libre de errores humanos, y entregado de forma segura a los servidores de producción.

**¿Cuál es la diferencia entre pipeline de producción y CI/CD?**
CI/CD (Integración Continua / Despliegue Continuo) es la metodología fundamental y la columna vertebral del pipeline. El pipeline de producción es el nombre del sistema amplio que, además de CI/CD, abarca el aprovisionamiento de entornos, escaneos de seguridad (DevSecOps), mecanismos de aprobación y herramientas de observabilidad.

**¿Con qué herramientas se construye el pipeline de producción?**
GitHub y GitLab para el control de versiones; GitHub Actions, Jenkins y ArgoCD para la orquestación; Docker para el empaquetado; y Kubernetes y Terraform para la infraestructura son las herramientas más comunes.

**¿Se producen interrupciones en el sistema durante el despliegue?**
En un pipeline de producción bien diseñado se utilizan métodos de despliegue Azul-Verde o Canary; de esta manera, los usuarios son transferidos a la nueva versión sin sentir interrupciones (cero tiempo de inactividad).


## Términos relacionados
- [Deployment](/es/dictionary/deployment/)
- [Data Pipeline](/es/dictionary/data-pipeline/)
- [Cloud Computing](/es/dictionary/cloud-computing/)
- [Tech Stack](/es/dictionary/tech-stack/)
- [Git Push](/es/dictionary/git-push/)
- [Runtime](/es/dictionary/runtime/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/production-pipeline/
