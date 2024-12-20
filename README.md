Component for HomeAssistant to integrate W115 Smartplug from DLink into Home Assistant.
Based on https://github.com/jonassjoh/dspW245

You have to setup the switch according to his instructions.

Copy the "smartplug" folder into "custom_components"

Setup the switch with:
'''
switch:
  - platform: smartplug
    name: W115-SmartPlug
    host: "YOUR-IP"
    pin: "xxxxxx"
'''
