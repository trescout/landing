# Plataforma de automatización de TI sin agentes

Ansible es una herramienta sin agentes que realiza la configuración de sistemas, el despliegue de software y la automatización de TI a través de archivos YAML simples.

- ★ 70.299
- GitHub Trending · 2026-07-04

## ¿Qué hace esta herramienta?
Ansible es una herramienta sin agentes que realiza la configuración de sistemas, el despliegue de software y la automatización de TI a través de archivos YAML simples y legibles. Le permite gestionar su infraestructura como código y estandarizar tareas complejas.

## ¿Para quién es?
Aquellos que deseen configurar múltiples servidores simultáneamente y automatizar procesos de gestión de manera confiable.

## Qué no esperar
Aquellos que solo deseen ejecutar tareas simples en una única máquina local y no necesiten una infraestructura de automatización.

## Aspectos destacados
- No requiere la instalación de agentes en los servidores de destino.
- Mantiene las configuraciones en formato YAML, que es fácil de leer y escribir.
- Ofrece un amplio soporte de integración con miles de módulos listos para usar.

## Primer flujo de uso
- Instale el paquete de Ansible en su nodo de control.
- Agregue las direcciones IP de los servidores que va a gestionar al archivo de configuración (inventario).
- Configure la autenticación basada en claves para garantizar el acceso SSH a los servidores de destino.
- Ejecute una prueba de ping en todos los servidores para verificar la conexión.

## Inicio seguro

## Primer prompt
¿Cómo instalar Nginx en todos los servidores web con Ansible?

## Instalación
**pip (PyPI)**

```
pip install ansible
```

**macOS (Homebrew)**

```
brew install ansible
```


## Ejecución
**Ejecute el script del libro de jugadas de Ansible**

```
ansible-playbook site.yml
```


## Enlaces
- Repositorio en GitHub →
- README oficial de Ansible →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/ansible/
