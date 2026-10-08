# Reinforcement learning environment for Pollen Robotics Microduck

Developed by Pollen Robotics, microduck_rl provides reinforcement learning training environments and control policies on MuJoCo and mjlab for the Microduck robot platform.

- ★ 2,281
- Python
- GitHub Trending · 2026-08-31

## Updates

- **September 27, 2026:** Stars 1,001 → 2,281.

## What you get

- Realistic MuJoCo physics simulation: The ability to simulate the robot's joint torques, friction, and gravity effects at high speed.
- Ready-to-use locomotion and balance tasks: Pre-defined reward functions for walking (walk), balancing, and obstacle traversal scenarios.
- Suitability for Sim-to-Real transfer: Noise-resistant control policies that can be easily transferred to physical Microduck hardware.
- Modern reinforcement learning algorithms: training infrastructure powered by PPO (Proximal Policy Optimization) and SAC.
- Visual 3D evaluation interface: Real-time monitoring of the trained robot agent's movements in a 3D simulator on the screen.

## Installation

**Cloning the repository and setting up the simulation environment**

```
git clone https://github.com/pollen-robotics/microduck_rl.git
cd microduck_rl
pip install -e .
```

## Running it

**Running training or policy evaluation**

```
python -m microduck_rl.train --task walk
# Eğitilen politikayı simülatörde izleme:
python -m microduck_rl.enjoy --checkpoint checkpoint.pt
```

## Technical architecture and working principle

- MuJoCo and mjlab Physics Layer: XML/MJCF files that define the robot's kinematics, joint limits, and actuator models.
- Gymnasium-Compatible Observation and Action Spaces: Standardization of motor angles, velocities, accelerometer (IMU) data, and target torque vectors.
- Domain Randomization Mechanism: Training models robust to the real world by randomly varying friction coefficients, mass distribution, and sensor noises.

## Physics simulation and robotic control policies

- Preventing Hardware Damage: Completely eliminate the robot's risks of falling and leg breakage in a virtual environment before moving to the physical robot.
- Training Millions of Steps in Accelerated Time: Completing days of training in hours by running the physics engine 100 times faster than real-time.
- Custom Mission and Terrain Design: Test the robot's adaptability to various terrains by adding stairs, sloped floors, and slippery surfaces.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to train a walking policy for the Microduck robot using Pollen Robotics' microduck_rl library. Could you explain the steps for configuring the MuJoCo environment, initiating the training command with the PPO algorithm, and transferring the resulting control policy to the physical robot?

## Frequently asked questions

- Is it necessary to have a physical Microduck robot to run microduck_rl? No. The codebase can be run entirely virtually within the MuJoCo simulator; you can watch a 3D simulation of the robot on your computer.
- Is GPU support required? MuJoCo also runs quite fast on the CPU; however, when training reinforcement learning with parallel environments, a CUDA-enabled GPU speeds up the process significantly.
- How is the trained model transferred to the physical robot? Once training is complete, the generated ONNX or PyTorch checkpoint file is loaded into Microduck's onboard control computer and directly connected to the motor torques.
- Does it support different robot models? microduck_rl is primarily optimized for Microduck; however, thanks to its modular structure, it can be adapted to similar bipedal or quadruped robot MJCF models.

## Related dictionary terms

- [Reinforcement Learning](https://trescout.com/en/dictionary/reinforcement-learning/)
- [CPU](https://trescout.com/en/dictionary/cpu/)
- [GPU](https://trescout.com/en/dictionary/gpu/)
- [API](https://trescout.com/en/dictionary/api/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Robotics researchers, mechatronics engineers, reinforcement learning experts, and hobbyists.
- **License:** Apache-2.0 (Açık kaynak lisansı)
- **Framework:** Python, MuJoCo & mjlab Robotics Framework
- **Platforms:** Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/pollen-robotics/microduck_rl)
- [Read in Turkish →](https://trescout.com/discover/microduck-rl/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/microduck-rl/
