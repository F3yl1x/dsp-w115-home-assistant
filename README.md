Component for HomeAssistant to integrate W115 Smartplug from DLink into Home Assistant.
Based on https://github.com/jonassjoh/dspW245

You have to setup the switch according to his instructions.

Copy the "smartplug" folder into "custom_components"

Setup the switch with:
```
switch:
  - platform: smartplug
    unique_id: switch.w115-smartplug
    host: "192.168.3.172"
    pin: "792417"
```
