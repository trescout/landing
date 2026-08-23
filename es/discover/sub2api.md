# Gestione las suscripciones de IA desde un único centro

Sub2API es un servicio de migración de código abierto que combina diferentes assinaturas de IA, como Claude, OpenAI, Gemini y Grok, en una interfaz única. Embora permitir a los usuarios partilhar os custodes de subscrição, oferece a oportunidade de utilizar estos serviços de forma integrada con as ferramentas existentes.

- ★ 38.841
- Go
- GitHub Trending · 2026-08-23

## Qué aporta
- Combina diferentes suscripciones de IA en una sola interfaz
- Le ayuda a asignar los costos de suscripción de manera eficiente
- Ofrece la oportunidad de trabajar integrado con herramientas existentes.

## Instalación
**instalación automática**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Instalación con Docker**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```


## Ejecución
**Iniciar el servicio**

```
docker compose up -d
```

**Ver contraseña de administrador**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```


## Si no programa
¿Cómo puedo configurar diferentes servicios de IA como Claude, OpenAI, Gemini y Grok a través de una única puerta de enlace API utilizando la plataforma Sub2API? Explique los pasos básicos que debo seguir para asignar eficientemente mis cuotas de suscripción e integrarlas con mis herramientas de software existentes. Además, resuma las cuestiones legales y técnicas a las que debo prestar atención para cumplir con los términos de servicio de proveedores como Anthropic al utilizar esta plataforma.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/sub2api/
