Installation instructions using Arduino IDE Boards Manager

Starting with 1.6.4, Arduino allows installation of third-party platform packages using Boards Manager. We have packages available for Windows, Mac OS, and Linux (32 and 64 bit).

    Install the current upstream Arduino IDE at the 1.8 level or later. The current version is at the Arduino website.
    Start Arduino and open Preferences window.
    Enter https://dl.espressif.com/dl/package_esp32_index.json into Additional Board Manager URLs field. You can add multiple URLs, separating them with commas.
    Open Boards Manager from Tools > Board menu and install esp32 platform (and don't forget to select your ESP32 board from Tools > Board menu after installation).


Download
https://github.com/LilyGO/LORA-ESP32-OLED

Extract zip files and copy them to the liberary folder of arduino.
	
	
	
Arduino IDE for ESP32 https://github.com/espressif/arduino-esp32#installation-instructions
LoRa receive code and other examples : https://github.com/LilyGO/LORA-ESP32-...