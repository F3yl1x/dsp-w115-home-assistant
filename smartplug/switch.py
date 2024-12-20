from homeassistant.components.switch import SwitchEntity
from .smartplug import SmartPlug

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Smart Plug switch."""
    host = config.get("host")
    pin = config.get("pin")
    unique_id = config.get("unique_id")
    name = config.get("name")
    plug = SmartPlug(host, pin, hass)
    await plug.connect(hass)
    plug.send_upgrade()
    plug.send_login()
    async_add_entities([SmartPlugSwitch(plug, unique_id, name)])

class SmartPlugSwitch(SwitchEntity):
    def __init__(self, plug, unique_id, name):
        self.plug = plug
        self._state = False
        self._unique_id = unique_id
        self._name = name

    @property
    def unique_id(self):
        """
        Gibt die eindeutige ID der Entität zurück.
        """
        return self._unique_id

    @property
    def name(self):
        return self._name

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
