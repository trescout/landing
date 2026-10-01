# What is ADB?

> Android Debug Bridge

ADB (Android Debug Bridge) is a tool that enables communication for commands and debugging between a computer and an Android device.

## Definition and Word Origin
Debug means debugging and bridge means bridge. ADB communicates between the client on the computer and the adb daemon on the device; it is used for application installation, log collection, debugging, and limited device management operations. It is part of the Android SDK Platform-Tools package.

## How to Know and Use in Daily Life?
Development: App installation and logging.Test: Multi-device testing.Customization: Advanced settings.

## Technical Depth and Architecture
Triple layout:

## Frequently Mixed Things
It is thought to be a file transfer. It only copies, ADB interferes with the system. The difference in privileges is significant.

## Use in Different Disciplines
Cable: The line carrying the signal.Interpreter: The language of both sides.Controller: Remote management.

## Frequently Asked Questions
**Can everyone use it?**
Basic commands can be learned; however, especially adb shell and deletion operations require technical knowledge. It is necessary to verify the effect of the command before running it.

**Can it be wireless?**
Yes. On supported Android versions, connection can be established over Wi-Fi after pairing with the device. Stability and speed depend on the quality of the local network.

**Is it safe?**
If you have the device, yes. Confirmation is not granted for a device plugged into an unknown computer.

**What is the difference of Fastboot?**
ADB communicates with the operating system while Android is running. Fastboot, on the other hand, is used for partition image or firmware operations while the device is in bootloader mode; supported commands and the unlocking process vary depending on the device.


## Related terms
- [CLI](/en/dictionary/cli/)
- [SDK](/en/dictionary/sdk/)
- [Emulator](/en/dictionary/emulator/)

## Related tools
- [Universal Android Debloater Next Generation](/en/discover/universal-android-debloater-next-generation/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/adb/
