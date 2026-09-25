# ¿Qué es la Extensibilidad (Extensibility)?

> Inglés: Extensibility · Etimología: latín extendere (extender, alargar)

**Categoría:** Dev  
**Última actualización:** 2026-09-22

La extensibilidad (extensibility) es una propiedad de diseño del software que permite incorporar nuevas funciones, conectores y complementos sin necesidad de modificar el código fuente del núcleo de la aplicación.

## Definición y etimología
El término procede del latín extendere, que significa estirar o desplegar. En la ingeniería de software actual, es la piedra angular del principio Abierto/Cerrado de SOLID: las entidades deben estar abiertas a la extensión pero cerradas a la modificación. Se diseñan interfaces y mecanismos de enlace que admiten nuevas capacidades sin riesgo de romper la lógica central.

## Contexto cotidiano e uso práctico
Casos habituales de extensibilidad en el software diario :
- **Editores de Código:** VS Code conserva un rendimiento óptimo permitiendo que la comunidad agregue extensiones de depuración y sintaxis.- **Navegadores Web:** Extensiones de navegador que enriquecen la navegación con traductores o herramientas de seguridad.- **Gestores de Contenidos:** Plataformas como WordPress o Drupal, cuyo valor reside en la gran oferta de plugins y plantillas modulares.

## Profundidad técnica y arquitectura
Estrategias clave para lograr un sistema extensible :
- **Ganchos (Hooks) y Callbacks:** Puntos de interrupción en el flujo donde módulos externos registran su lógica.- **Inversión de Control e Interfaces:** Desacoplamiento entre la capa consumidora y las implementaciones de los plugins.- **Comunicaciones por Eventos:** Publicación de estados a través de buses de eventos desacoplados.- **Sandboxing con WASM:** Ejecución aislada de código de terceros para prevenir fugas de memoria o vulneraciones de seguridad.

## Perspectivas interdisciplinares
Paralelismos en otras actividades :
- **Arquitectura:** Estructuras modulares preparadas para ampliaciones laterales sin comprometer muros maestros.- **Bricolaje:** Taladros multifunción que permiten acoplar cabezales de lija, sierra o destornillador.- **Lego:** Bloques con enganches normalizados que permiten construir estructuras complejas sin alterar los bloques individuales.

## Por analogía
Es como una navaja suiza: el cuerpo central se mantiene sólido y compacto, pero cuenta con ranuras preparadas para acoplar nuevas herramientas según la situación.

## Preguntas frecuentes

**¿Conviene que todo software sea extensible?**  
No; introducir abstracciones de extensibilidad sin una necesidad clara añade complejidad innecesaria al código.

**¿En qué se diferencian extensibilidad y mantenibilidad?**  
La mantenibilidad evalúa lo sencillo que es reparar el código base; la extensibilidad evalúa lo fácil que es añadir nuevas funciones sin alterar dicho código.

**¿Cómo se protege el sistema contra plugins defectuosos?**  
Aislando los complementos en procesos independientes o entornos aislados tipo WASM con permisos controlados.

**¿Qué papel desempeñan las APIs en este modelo?**  
Definen las reglas y contratos estables que los módulos externos deben cumplir para interactuar con la aplicación anfitriona.

## Términos relacionados
- [Plugin](/es/dictionary/plugin/)
- [Emitter](/es/dictionary/emitter/)
- [Tools](/es/dictionary/tools/)

---
Fuente: Diccionario Tecnológico TreScout · https://trescout.com/es/dictionary/extensibility/
