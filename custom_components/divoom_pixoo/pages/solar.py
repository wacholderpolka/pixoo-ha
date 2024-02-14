from homeassistant.helpers.template import Template
from homeassistant.exceptions import TemplateError

def solar(pixoo, hass, page_data, FONT_PICO_8, FONT_GICKO, FONT_THIN):
    for solar in page_data["PV"]:
        pixoo.clear()
        try:
            rendered_power = int(Template(solar['power'], hass).async_render())
            rendered_storage = int(Template(solar['storage'], hass).async_render())
            rendered_discharge = int(Template(solar['discharge'], hass).async_render())
            rendered_powerhousetotal = int(Template(solar['powerhousetotal'], hass).async_render())
            rendered_vomNetz = int(Template(solar['vomNetz'], hass).async_render())
            rendered_time = str(Template(solar['time'], hass).async_render())
        except TemplateError as e:
            _LOGGER.error("Template render error: %s", e)
            return  # Stop execution if there is a template error

        green = (4, 204, 2) #discharge
        red = (255, 0, 68) #discharge
        grey = (131, 131, 131) #power vomNetz
        white = (255, 255, 255) #time
        yellow = (255, 175, 0) #power
        blue = (0, 123, 255) #powerhousetotal

        #Time
        pixoo.draw_text(rendered_time, (44, 1), white, FONT_PICO_8)

        #Power
        pixoo.draw_image("/config/custom_components/divoom_pixoo/img/sunpower.png", (1, 0))

        if rendered_power >= 1:
            pixoo.draw_text(f'{rendered_power}', (22, 5), yellow, FONT_THIN)
        else:
            pixoo.draw_text(f'{rendered_power}', (22, 5), grey, FONT_THIN)

        if rendered_discharge < 0: 
            pixoo.draw_text(f'{rendered_discharge}', (18, 21), red, FONT_THIN)
        else:
            pixoo.draw_text(f'{rendered_discharge}', (22, 21), green, FONT_THIN)

        if rendered_storage >= 0:
            pixoo.draw_image("/config/custom_components/divoom_pixoo/img/akku00-20.png", (1, 16))
        if rendered_storage >= 20:
            pixoo.draw_image("/config/custom_components/divoom_pixoo/img/akku20-40.png", (1, 16))
        if rendered_storage >= 40:
            pixoo.draw_image("/config/custom_components/divoom_pixoo/img/akku40-60.png", (1, 16))
        if rendered_storage >= 60:
            pixoo.draw_image("/config/custom_components/divoom_pixoo/img/akku60-80.png", (1, 16))
        if rendered_storage >= 80:
            pixoo.draw_image("/config/custom_components/divoom_pixoo/img/akku80-100.png", (1, 16))

        pixoo.draw_text(f"{rendered_storage}%", (50, 22), white, FONT_PICO_8) #FONT_PICO_8

        pixoo.draw_image("/config/custom_components/divoom_pixoo/img/haus.png", (1, 32))
        
        if rendered_powerhousetotal < 0:
            pixoo.draw_text(f"{rendered_powerhousetotal}", (18, 37), blue, FONT_THIN)
        else
            pixoo.draw_text(f"{rendered_powerhousetotal}", (22, 37), blue, FONT_THIN)
        

        pixoo.draw_image("/config/custom_components/divoom_pixoo/img/industry.png", (1, 48))
        if rendered_vomNetz < 0:
            pixoo.draw_text(f'{rendered_vomNetz}', (18, 53), grey, FONT_THIN)
        else
            pixoo.draw_text(f'{rendered_vomNetz}', (22, 53), grey, FONT_THIN)
