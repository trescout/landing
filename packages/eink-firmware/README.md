# TreScout E-Ink Desk Radar · ESP32 Open-Source Hardware

An eye-friendly, distraction-free physical E-Ink desk gadget that sits on your desk and displays today's top open-source discoveries and daily tech intelligence from **[TreScout](https://trescout.com)**.

---

## 🛠️ Hardware Requirements (~$15-$20)

* **Microcontroller:** ESP32 NodeMCU / ESP32-C3 / Raspberry Pi Pico W
* **Display:** Waveshare 2.9" or 4.2" E-Paper Display Module (SPI)
* **Battery / Power:** Micro-USB / USB-C or small 500mAh LiPo battery (lasts 6+ months on Deep Sleep).

---

## 🔌 Pinout & Wiring (ESP32 ➔ Waveshare 2.9" E-Paper)

| E-Paper Pin | ESP32 GPIO Pin |
| :--- | :--- |
| **VCC** | 3.3V |
| **GND** | GND |
| **DIN (MOSI)** | GPIO 23 |
| **CLK (SCK)** | GPIO 18 |
| **CS** | GPIO 5 |
| **DC** | GPIO 17 |
| **RST** | GPIO 16 |
| **BUSY** | GPIO 4 |

---

## 🚀 How to Flash & Run (MicroPython)

1. Flash MicroPython onto your ESP32 (`esptool.py`).
2. Update `WIFI_SSID` and `WIFI_PASS` in `main.py` (or `config.json`).
3. Upload `main.py` using `mpremote` or `Thonny`:
   ```bash
   mpremote cp main.py :main.py
   mpremote reset
   ```
4. Every morning at 08:00, the ESP32 wakes up, connects to Wi-Fi, fetches the day's fresh report, refreshes the E-Ink screen, and goes into 24-hour ultra-low-power deep sleep.
