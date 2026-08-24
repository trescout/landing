# Workflows visuales y automatización con IA

n8n combina un canvas visual, código personalizado, agentes de IA y workflows en una plataforma de automatización fair-code. Admite despliegues autoalojados o en la nube y puede incluir distintos proveedores de modelos en los workflows.

- ★ 201.895
- GitHub Trending · 2026-08-23

## ¿Qué hace esta herramienta?
Con n8n puedes crear workflows en un canvas visual y ampliarlos con JavaScript, Python y paquetes npm. Las fuentes oficiales mencionan flexibilidad entre modelos de OpenAI, Anthropic, Google y de código abierto, además de aprobaciones humanas, observabilidad, acceso basado en roles y registros de auditoría. La plataforma puede desplegarse de forma autoalojada o en la nube.

## ¿Para quién es?
Equipos que quieren combinar el diseño visual de workflows con código personalizado y agentes de IA.

## Qué no esperar
Personas que solo buscan productos con licencia propietaria o que no quieren ampliar los workflows con código o configuración.

## Aspectos destacados
- Combina canvas visual, código personalizado y agentes de IA en los workflows.
- Se puede ampliar con JavaScript, Python y paquetes npm.
- Ofrece despliegue autoalojado y en la nube.
- Menciona aprobaciones humanas, observabilidad, acceso basado en roles y registros de auditoría.

## Primer flujo de uso
- Sigue el inicio rápido oficial con Docker para ejecutar n8n.
- Abre el editor en tu navegador mediante el puerto 5678.
- Crea tu primer workflow en el canvas visual.
- Añade código personalizado o un proveedor de modelos compatible según tus necesidades.

## Inicio seguro

## Primer prompt
Ayúdame a diseñar en el canvas visual un workflow que reciba una entrada, la procese con un modelo de IA y pase el resultado al siguiente paso.

## Instalación
**Crea el volumen de datos**

```
docker volume create n8n_data
```


## Ejecución
**Inicia el contenedor Docker de n8n**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```


## Enlaces
- Repositorio en GitHub →
- Repositorio oficial de GitHub de n8n →
- Documentación oficial de n8n →
- Repositorio de documentación de n8n →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/n8n/
