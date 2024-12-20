from homeassistant.components.switch import SwitchEntity
from .smartplug import SmartPlug

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Smart Plug switch."""
    host = config.get("host")
    pin = config.get("pin")
    plug = SmartPlug(host, pin)
    async_add_entities([SmartPlugSwitch(plug)])

class SmartPlugSwitch(SwitchEntity):
    def __init__(self, plug):
        self.plug = plug
        self._state = False

    @property
    def name(self):
        return "D-Link Smart Plug"

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self.plug.set_led(1, True)
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        self.plug.set_led(1, False)
        self._state = False
        self.schedule_update_ha_state()

    def update(self):
        status = self.plug.device_status()
        self._state = status["led_state"] == 1
