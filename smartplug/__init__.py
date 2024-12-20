from homeassistant.core import HomeAssistant

DOMAIN = "smartplug"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Smart Plug component."""
    hass.data[DOMAIN] = {}
    return True
