# Entorno de aprendizaje por refuerzo para Pollen Robotics Microduck

Desarrollado por Pollen Robotics, microduck_rl proporciona entornos de capacitación de aprendizaje reforzado y políticas de control en MuJoCo y mjlab para la plataforma robótica Microduck.

- ★ 2.281
- Python
- GitHub Trending · 2026-08-31

## Actualizaciones

- **27 de septiembre de 2026:** Estrellas 1,001 → 2,281.

## Qué aporta

- Simulación física realista de MuJoCo: capacidad de simular los pares de torsión de las articulaciones, la fricción y los efectos de la gravedad del robot a alta velocidad.
- Tareas de locomoción y equilibrio listas para usar: funciones de recompensa predefinidas para escenarios de caminar, equilibrar y superar obstáculos.
- Adecuado para transferencia Sim-to-Real: Políticas de control resistentes al ruido que se pueden transferir fácilmente al hardware físico Microduck.
- Algoritmos modernos de aprendizaje por refuerzo: infraestructura de capacitación respaldada por PPO (optimización de políticas próximas) y SAC.
- Interfaz de evaluación visual 3D: Monitoreo instantáneo de los movimientos del agente robótico entrenado en el simulador 3D en la pantalla.

## Instalación

**Clonar el repositorio y configurar el entorno de simulación**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```

## Ejecución

**Ejecutar capacitación o evaluación de políticas**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```

## Arquitectura técnica y principio de funcionamiento

- MuJoCo y mjlab Physics Layer: archivos XML/MJCF que definen la cinemática del robot, los límites de las articulaciones y los modelos de actuador.
- Espacios de observación y acción compatibles con gimnasios: estandarización de ángulos de motor, velocidades, datos del acelerómetro (IMU) y vectores de par objetivo.
- Mecanismo de aleatorización de dominio: entrenamiento de modelos robustos del mundo real variando aleatoriamente los coeficientes de fricción, la distribución de masa y el ruido del sensor.

## Políticas de simulación física y control de robótica.

- Prevención de daños al hardware: resuelva los riesgos de caídas de robots y fracturas de piernas en un entorno completamente virtual antes de pasar al robot físico.
- Entrenamiento de millones de pasos en tiempo acelerado: Completa días de entrenamiento en horas operando el motor de física 100 veces más rápido que en tiempo real.
- Diseño personalizado de misión y terreno: pruebe la adaptabilidad del robot a diferentes terrenos agregando escaleras, pendientes y superficies resbaladizas.

## Si no programa

🤖 Pegue esto en su agente (Claude Code · Codex · Antigravity)

Quiero entrenar una política de caminata para el robot Microduck utilizando la biblioteca microduck_rl de Pollen Robotics. ¿Puede explicar los pasos sobre cómo configurar el entorno MuJoCo, inicializar el comando de entrenamiento con el algoritmo PPO y transferir la política de control resultante al robot físico?

## Preguntas frecuentes

- ¿Es necesario tener un robot Microduck físico para ejecutar microduck_rl? No. El código base se puede ejecutar de forma completamente virtual en el simulador MuJoCo; Puedes ver la simulación 3D del robot en tu computadora.
- ¿Se requiere compatibilidad con GPU? MuJoCo también se ejecuta bastante rápido en la CPU; Sin embargo, cuando se entrena el aprendizaje por refuerzo con entornos paralelos, una GPU compatible con CUDA acelera significativamente el proceso.
- ¿Cómo se transfiere el modelo entrenado al robot físico? Cuando se completa la capacitación, el archivo de punto de control ONNX o PyTorch generado se carga en la computadora de control integrada de Microduck y se conecta directamente a los pares del motor.
- ¿Admite diferentes modelos de robots? microduck_rl está optimizado principalmente para Microduck; Sin embargo, gracias a su estructura modular, se puede adaptar a modelos similares de robot bípedo o cuadrúpedo MJCF.

## Términos relacionados del glosario

- [Reinforcement Learning](https://trescout.com/es/dictionary/reinforcement-learning/)
- [CPU](https://trescout.com/es/dictionary/cpu/)
- [GPU](https://trescout.com/es/dictionary/gpu/)
- [API](https://trescout.com/es/dictionary/api/)
- [Open Source](https://trescout.com/es/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/es/dictionary/artificial-intelligence/)

- **Para quién es:** Investigadores de robótica, ingenieros de mecatrónica, expertos en aprendizaje por refuerzo y aficionados.
- **Licencia:** Apache-2.0 (Açık kaynak lisansı)
- **Marco:** Marco de robótica Python, MuJoCo y mjlab
- **Plataformas:** Linux, Mac OS, Windows

## Enlaces

- [Repositorio en GitHub →](https://github.com/pollen-robotics/microduck_rl)
- [Leer en turco →](https://trescout.com/discover/microduck-rl/)

TreScout no desarrolló esta herramienta · la encontramos en las tendencias de GitHub y la presentamos. Esta página describe el repositorio tal como estaba el 2026-08-31: El número de estrellas y nuestro texto son de ese día, el repositorio puede haber cambiado desde entonces. Consulte el enlace del repositorio para ver el estado actual. Esta página se **tradujo automáticamente** del original en turco · prevalece la versión turca.

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/microduck-rl/
