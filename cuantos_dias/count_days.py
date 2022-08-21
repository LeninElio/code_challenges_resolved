"""

/*
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar
     ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

"""
import string


def valida():
    while True:
        fec_01x = str(input('Ingrese la primera fecha en el formato [dd/MM/yyyy]:'))
        fec_02x = str(input('Ingrese la segunda fecha en el formato [dd/MM/yyyy]:'))
        try:
            if '/' not in fec_01x or '/' not in fec_02x:
                print('Ingrese una fecha valida')
                exit()
            else:
                pass

            fec_01x = fec_01x.split('/')
            fec_02x = fec_02x.split('/')

            if fec_02x[0] == '' or int(fec_02x[0]) > 31 or fec_02x[0] in string.ascii_letters \
                    or fec_02x[1] == '' or int(fec_02x[1]) > 12 or fec_02x[1] in string.ascii_letters \
                    or fec_02x[2] == '' or fec_02x[2] in string.ascii_letters or len(fec_02x[2]) > 4 \
                    or len(fec_02x[1]) > 2 or len(fec_02x[0]) > 2:
                print('Ingrese un dia valido, error en dia')
                exit()
            else:
                pass

            if len(fec_01x[2]) > 4 or fec_01x[0] == '' or int(fec_01x[0]) > 31 or fec_01x[0] in string.ascii_letters \
                    or fec_01x[1] == '' or int(fec_01x[1]) > 12 or fec_01x[1] in string.ascii_letters \
                    or fec_01x[2] == '' or fec_01x[2] in string.ascii_letters or len(fec_01x[1]) > 2\
                    or len(fec_01x[0]) > 2:
                print('Ingrese un dia valido, error en dia')
                exit()
            else:
                pass

            return fec_01x, fec_02x
        except Exception as e:
            print("Debe ingresar una fecha valida...", e)
            exit()


fec_01, fec_02 = valida()


# fec_01 = "25/01/2021"
# fec_02 = "20/04/2022"

# fec_01x = fec_01x.split('/')
# fec_02x = fec_02x.split('/')


def mayor():
    if int(fec_01[2]) > int(fec_02[2]):
        return fec_01, fec_02
    elif int(fec_02[2]) > int(fec_01[2]):
        return fec_02, fec_01
    else:
        if int(fec_01[1]) > int(fec_02[1]):
            return fec_01, fec_02
        elif int(fec_02[1]) > int(fec_01[1]):
            return fec_02, fec_01
        else:
            if int(fec_01[0]) > int(fec_02[0]):
                return fec_01, fec_02
            elif int(fec_02[0]) > int(fec_01[0]):
                return fec_02, fec_01
            else:
                return 'Misma', 'fecha'


may_fecha, men_fecha = mayor()

mapa_mes = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
            '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}


def bisiesto(bisi):
    bisi = int(bisi)
    if bisi % 400 == 0 or (bisi % 4 == 0 and bisi % 100 != 0):
        return True
    else:
        return False


def febrero(ret_an):
    mapa_feb = mapa_mes
    if bisiesto(ret_an):
        mapa_feb['02'] = str(29)
    return mapa_feb


def retorna_num(da, mes, ani):
    da = int(da)
    suma = 0
    for cl, vl in febrero(ani).items():
        suma += int(vl)
        if cl == mes:
            retorno = suma - (int(vl) - da)
            return retorno


residuo = []
dif_an = int(may_fecha[2])
while dif_an >= int(men_fecha[2]):
    residuo.append(dif_an)
    dif_an -= 1

valores = []
for an in residuo:
    if len(residuo) <= 1:
        mayor_aio = retorna_num(may_fecha[0], may_fecha[1], may_fecha[2])
        menor_aio = retorna_num(men_fecha[0], men_fecha[1], men_fecha[2])
        resta_dias = mayor_aio - menor_aio
        valores.append(resta_dias)
    elif an == residuo[-1]:
        if bisiesto(an):
            bis = 366
            men = retorna_num(men_fecha[0], men_fecha[1], men_fecha[2])
            valores.append(bis - men)
        else:
            bis = 365
            men = retorna_num(men_fecha[0], men_fecha[1], men_fecha[2])
            valores.append(bis - men)
    elif an == residuo[0]:
        if bisiesto(an):
            bis = 366
            may = retorna_num(may_fecha[0], may_fecha[1], may_fecha[2])
            valores.append(may)
        else:
            bis = 365
            may = retorna_num(may_fecha[0], may_fecha[1], may_fecha[2])
            valores.append(may)
    else:
        if bisiesto(an):
            bis = 366
            valores.append(bis)
        else:
            bis = 365
            valores.append(bis)

sumas = 0
for x in valores:
    sumas += int(x)

men_fecha = '/'.join(men_fecha)
may_fecha = '/'.join(may_fecha)

print(f'El {men_fecha} y {may_fecha} están separados por: ')
print(f'☸ {sumas} dias')
print(f'☸ {round(sumas / 365, 2)} años')
print(f'☸ {round(sumas / 30, 2)} meses')
print(f'☸ {round(sumas / 7, 2)} semanas')
print(f'☸ {sumas * 24} horas')
print(f'☸ {sumas * 24 * 60} minutos')
print(f'☸ {sumas} * 10^4 * 8.64 segundos')
