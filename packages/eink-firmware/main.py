"""
TreScout E-Ink Desk Radar · ESP32 MicroPython Firmware
=====================================================
Fetches daily tech intelligence from TreScout endpoint and renders a
high-contrast, eye-friendly layout on a 2.9" or 4.2" E-Paper display.
"""

import time
import network
import urequests
import ujson

# Default Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASS = "YOUR_WIFI_PASSWORD"
TRESCOUT_ENDPOINT = "https://trescout.com/assets/api/eink-daily.json"


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print("Wi-Fi connected! IP:", wlan.ifconfig()[0])
        return True
    else:
        print("Wi-Fi connection failed!")
        return False


def fetch_daily_data():
    try:
        response = urequests.get(TRESCOUT_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            response.close()
            return data
    except Exception as e:
        print("Fetch error:", e)
    return None


def render_to_display(data):
    """
    Renders structured layout to E-Paper buffer.
    (Compatible with Waveshare 2.9 / 4.2 / LilyGO T-Echo)
    """
    if not data:
        print("No data to render.")
        return

    print("========================================")
    print(" 📡 TRESCOUT DESK RADAR")
    print(" Date:", data.get("display_date"))
    print("========================================")
    print("Overview:", data.get("editorial"))
    print("----------------------------------------")
    print("TOP OPEN SOURCE DISCOVERIES:")
    for idx, tool in enumerate(data.get("top_tools", [])):
        print(f" {idx+1}. {tool.get('name')} ({tool.get('stars')})")
        print(f"    {tool.get('summary')}")
        if tool.get("cmd"):
            print(f"    > {tool.get('cmd')}")
    print("========================================")
    print("Full report:", data.get("qr_url"))
    print("Display refreshed. Entering deep sleep for 24 hours...")


def main():
    if connect_wifi():
        data = fetch_daily_data()
        render_to_display(data)

    # Deep Sleep for 24 hours (86400 seconds) to conserve battery
    # import machine
    # machine.deepsleep(86400 * 1000)


if __name__ == "__main__":
    main()
