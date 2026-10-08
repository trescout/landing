# ¿Qué es End-to-End Testing?

*Glosario · Dev · Última actualización: 22 de septiembre de 2026*

> E2E Testing

Las pruebas de extremo a extremo (E2E, por sus siglas en inglés) consisten en probar la aplicación de principio a fin tal como lo haría un usuario.

## Definición y origen de la palabra

De punta a punta significa de extremo a extremo. Se prueba el todo y no la pieza: se entra, se presiona el botón, los datos van, el resultado regresa. Es la puerta de conformidad previa a la publicación.

***Analogía:** Es como intentar girar la llave y ponerse en marcha en lugar del motor.*

## ¿Cómo saberlo y utilizarlo en la vida diaria?

**Publicación:** Ronda previa a la versión.
**Tienda:** Ruta de compra.
**Formulario:** Flujo de registro.

## Profundidad técnica y arquitectura

Diseño:

**Camino crítico:** Flujo monetizado primero.
**Automatización:** Herramienta que controla el navegador.
**Datos:** Cuenta de prueba y restablecimiento.

Ejemplo:

```
test("giriş", async () => {
  await sayfa.goto("/giris");
  await bekle("#panel");
});
```

Motivo de la lentitud: Se abre un navegador real. Se elige el camino crítico, no se prueba todo.

## Cosas frecuentemente mezcladas

Se confunde con una prueba unitaria. Una mira esa pieza, la otra mira el todo. Una es la prueba de un tornillo, la otra la de conducción.

## Uso en diferentes disciplinas

**Coche:** Partir de la llave.
**Ensayo:** Repaso general.
**Final:** Ensayo de transmisión.

## Preguntas frecuentes

**¿Por qué no se hace solo esto?**

Es lento, el origen de la falla es difuso. Se usa junto con la unidad.

**¿Con qué frecuencia se ejecuta?**

Antes de la transmisión y por la noche. Un subconjunto crítico se ejecuta en cada commit.

**¿Quién lo escribe?**

El desarrollador y el evaluador lo escriben juntos. Tiene un propietario claro.

**¿Es frágil?**

Se rompe cuando cambia la interfaz. Se escribe de forma selectiva y resistente.

## Términos relacionados

- [Unit Testing](https://trescout.com/es/dictionary/unit-testing/)
- [Testing Framework](https://trescout.com/es/dictionary/testing-framework/)
- [Web Interface](https://trescout.com/es/dictionary/web-interface/)

## Herramientas relacionadas

- [Cypress](https://trescout.com/es/discover/cypress/)
- [E2e](https://trescout.com/es/discover/e2e/)

Esta explicación se redactó en lenguaje sencillo para TreScout y se **tradujo automáticamente** del original en turco · prevalece la versión turca. Si algo le parece erróneo o incompleto, escriba a [hello@trescout.com](mailto:hello@trescout.com). [Leer en turco →](https://trescout.com/dictionary/end-to-end-testing/)

---
Fuente: TreScout Glosario · https://trescout.com/es/dictionary/end-to-end-testing/
