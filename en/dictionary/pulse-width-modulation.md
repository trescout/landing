# What is Pulse-Width Modulation?

*Development · Last updated: November 16, 2026*

> Pulse-Width Modulation

It is a signal conditioning method that controls power and screen brightness by changing the voltage duration of digital signals.

## Overview

Pulse-Width Modulation (PWM) is a technique for adjusting the average voltage by rapidly changing the on and off times of an electrical signal. Instead of directly lowering the voltage level, you control the power by turning it on and off within milliseconds. It is widely used in many hardware systems, from screen brightness settings to motor speed control.

***Analogy:** You can think of it like turning your switch on and off a thousand times a second to lower the light level of a lamp. The longer the switch stays on, the brighter your eyes perceive the light.*

## How it works

The duty cycle, which is the ratio of the time the signal is high to the total period, is varied. When the duty cycle is 50%, half of the power is transmitted. Thanks to this high-speed switching, precise power management is achieved without energy loss.

## Where it is used

It is frequently preferred in brightness control of OLED and LCD screens, speed adjustments of cooling fans, and electric motor control.

## Commonly confused with

It can be confused with direct analog voltage adjustment. PWM does not lower the voltage level itself; it manages the average power by changing the active duration of the voltage.

## Questions and answers

**Why does PWM cause eye strain on screens?**

PWM screens with a low refresh rate create an imperceptible rapid flicker. This situation may cause eye strain and headaches in some users.

**How is a PWM signal generated?**

It is generated from digital output pins with the help of microcontrollers and dedicated hardware timers.

## Related terms

- [Single-Board Computers](https://trescout.com/en/dictionary/single-board-computers/)
- [IoT](https://trescout.com/en/dictionary/iot/)
- [CPU](https://trescout.com/en/dictionary/cpu/)
- [System Design](https://trescout.com/en/dictionary/system-design/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/pulse-width-modulation/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/pulse-width-modulation/
