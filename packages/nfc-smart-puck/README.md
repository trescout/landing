# TreScout NFC Smart Puck · Hardware & Tag Programming

Turn any \$0.50 NFC NTAG213/215 sticker or physical desktop coaster/puck into a physical **TreScout Instant Audio Briefing Trigger**.

---

## 📲 How It Works

1. Open `packages/nfc-smart-puck/puck-programmer.html` in Chrome on an Android phone or Web NFC-compatible browser.
2. Click **"📲 NFC Çipine Yazdır"**.
3. Hold the back of your phone to your NFC sticker or 3D-printed puck.
4. Done! Now, every morning when you place your phone on the desk puck, the 1-minute AI audio briefing automatically plays in your headphones.

---

## 📋 NDEF Payload Protocol
* **Record Type:** `URI`
* **Target:** `https://trescout.com/reports/?autoplay=audio&utm_source=nfc_puck`
