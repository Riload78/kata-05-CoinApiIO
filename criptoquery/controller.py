from criptoquery.view import validate
from criptoquery.models import criptos, fiats, get_rate
from criptoquery.view import output


class Controller:
    def mainloop(self):
        while True:
            cripto = validate(criptos, '¿Que moneda quieres?')
            fiat = validate(fiats, '¿En que moneda quieres?')

            status, data = get_rate(cripto, fiat)

            output(status, cripto, fiat, data)

            more_conversions = validate(('S','N'), '¿Quieres introducir mas monedas')
            if more_conversions != "S":
                break